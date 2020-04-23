from flask import Flask, jsonify, Blueprint
from src.dao import calendar

calendar_bp = Blueprint('calendar', __name__)


@calendar_bp.route('/getevents', methods=['GET'])
def usersHandler():
    responseData = []
    try:
        maxEvents = request.args.get('max')
        responseData = calendar.getMealEvents(max=maxEvents)
    except:
        responseData = calendar.getMealEvents()
    return jsonify({"response": responseData})
