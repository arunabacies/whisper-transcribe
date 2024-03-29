import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_cors import CORS
from config import Config_is


def create_app(config_class=Config_is):
    app = Flask(__name__, template_folder='templates')
    CORS(app)
    app.config.from_object(config_class)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = RotatingFileHandler('log_data.log', maxBytes=100000, backupCount=2)
    file_handler.setFormatter(formatter)
    logging.basicConfig(handlers=[file_handler], level=logging.DEBUG)
    logger = logging.getLogger('log_data.log')
    app.logger.addHandler(file_handler)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp)
    return app