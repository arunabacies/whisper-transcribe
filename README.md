# Mp3 file transcriber


[BASE MODEL]: <https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt>
[FLASK APP DEPLOYMENT]: <https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04>
[CELERY APP DEPLOYMENT]: <https://medium.com/sightwave-software/setting-up-nginx-gunicorn-celery-redis-supervisor-and-postgres-with-django-to-run-your-python-73c8a1c8c1ba>

## Installation
- Create .env file from env.sample
- Download Whisper base model here [BASE MODEL]
- Install all python packages from requirements.txt
    ```pip install -r requirements.txt```
- Set up redis
- Deploy the flask app application using nginx [FLASK APP DEPLOYMENT]
- Deploy celery using nginx [CELERY APP DEPLOYMENT]

## Endpoints
- /uploader
    Mp3 uploader web page
- /uploaded_data
    Get the processed media records