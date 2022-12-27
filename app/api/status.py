from flask import jsonify, request
from app.api import bp
from app import tasks

@bp.route('/demo', methods=['GET'])
def demo_mn():
    # tasks.daily_check.delay()
    return jsonify({"message": "Starting the background job"})