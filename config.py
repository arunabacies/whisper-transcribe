import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    BASE_URL = os.environ.get('BASE_URL')
    DEBUG = os.environ.get('DEBUG') or False
    PORT = os.environ.get('PORT')
    REDIS_URL = os.environ.get('REDIS_URL')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME_PROD')
    BUCKET_PATH = os.environ.get('BUCKET_PATH_PROD')
    

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME_DEV")
    # BUCKET_PATH = os.environ.get('BUCKET_PATH_DEV')


class TestConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME_TEST")
    # BUCKET_PATH = os.environ.get('BUCKET_PATH_DEV')


configs = dict(
    dev=DevelopmentConfig,
    prod=Config,
    test=TestConfig
)

Config_is = configs[os.environ.get('CONFIG', 'prod')]
