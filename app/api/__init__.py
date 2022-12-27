from flask import Blueprint

bp = Blueprint('api', __name__)
from app.api import status
from app.api import upload_file
