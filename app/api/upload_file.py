from flask import render_template, request
from werkzeug.utils import secure_filename
from app.api import bp
from config import Config_is
import json
import hashlib
import boto3
import redis
from app.tasks import *
redis_obj = redis.StrictRedis.from_url(Config_is.REDIS_URL, decode_responses=True)

s3_client = boto3.client('s3', aws_access_key_id=Config_is.AWS_ACCESS_KEY_ID, aws_secret_access_key=Config_is.AWS_SECRET_ACCESS_KEY)

def upload_file_to_s3(file_is):
    file_name = secure_filename(file_is.filename)
    hash_object = hashlib.sha256(file_name.encode('utf-8'))
    job_id = hash_object.hexdigest()[:255]
    try:
        s3_client.upload_fileobj(file_is,
            Config_is.S3_BUCKET_NAME,
            f"{Config_is.BUCKET_PATH}/{job_id}",
            ExtraArgs={"ACL": "public-read", "ContentType": file_is.content_type}
            )
        transcriber.delay({'job_id': job_id, 'file': file_name})
    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e
    return job_id

@bp.route('/uploader')
def upload_file_template():
   return render_template('uploader.html')

@bp.route("/upload", methods=["POST"])
def uploading_file():
    file = request.files['user_file']
    output = upload_file_to_s3(file) 
    if output:
        return f"successfully uploaded & the job id is {output}"

@bp.route("/uploaded_data", methods=["GET"])
def get_uploaded_data():
    result = []
    for r in redis_obj.keys():
        try:
            result.append(json.loads(redis_obj[r]))
        except Exception as e:
            print(r ,e)
    return render_template("results.html", result=result)