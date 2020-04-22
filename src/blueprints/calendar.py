from flask import Flask, jsonify, Blueprint
from src.dao import calendar

calendar_bp = Blueprint('calendar', __name__)


@calendar_bp.route('/getevents', methods=['GET'])
def usersHandler():
    calendar.getMealEvents(7)
    return jsonify({"response": "Events printed on console"})
