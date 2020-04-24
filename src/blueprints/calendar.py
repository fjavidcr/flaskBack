from flask import Flask, jsonify, Blueprint, request
from src.dao import calendar

calendar_bp = Blueprint('calendar', __name__)


@calendar_bp.route('/meals', methods=['GET'])
def meals():
    responseData = []

    try:
        maxEvents = request.args.get('max')
        print('max events: {}'.format(maxEvents))
    except:
        print('max events: default')

    if maxEvents:
        responseData = calendar.getMealEvents(max=maxEvents)
    else:
        responseData = calendar.getMealEvents()

    return jsonify(responseData)
