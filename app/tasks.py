from datetime import datetime, timedelta, date
import json
import os
import re
import time
import redis
from celery import Celery
import whisper
from app import create_app
from config import Config_is

redis_obj = redis.StrictRedis.from_url(Config_is.REDIS_URL, decode_responses=True)
app = create_app()
app.app_context().push()
app = Celery('tasks',
             broker=Config_is.REDIS_URL)

app.conf.timezone = 'UTC'
    


@app.task
def transcriber(data: dict):
    try:
        # Download File to Local storage
        start_time = time.time()
        if not os.path.exists(f"tmp/{data['job_id']}"):
            os.system(f"wget -O tmp/{data['job_id']} {Config_is.S3_BUCKET_NAME}.s3.us-east-1.amazonaws.com/{Config_is.BUCKET_PATH}/{data['job_id']}")
        file_size = os.stat(f"tmp/{data['job_id']}")  # get the file size
        data['download_time_in_seconds'] = float("{:.2f}".format(time.time() - start_time))
        data['file_size_in_mb'] = float(f'{file_size.st_size / 1000000:.2f}')
        data['file_downloaded'] = True
    except Exception as e:
        data['error'] = str(e)
        redis_obj.set(data['job_id'], json.dumps(data))
        return False
    s_time = time.time()
    model = whisper.load_model("base")
    try:
        text_result = model.transcribe(f"tmp/{data['job_id']}")
        data.update({'transcription_time_taken': time.time()-s_time, 'result': text_result})
    except Exception as e:
        data.update({'error': str(e)})
    redis_obj.set(data['job_id'], json.dumps(data))
    try:
        # Delete the processed video file
        os.remove(f"tmp/{data['job_id']}")
    except OSError:
        pass
    return True
