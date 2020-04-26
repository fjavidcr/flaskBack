from flask import Flask, jsonify, Blueprint, request
from src.dao.calendar import Calendar

calendar_bp = Blueprint('calendar', __name__)

calendar_dao = None


@calendar_bp.route('/meals', methods=['GET'])
def meals():
    global calendar_dao
    if not calendar_dao:
        calendar_dao = Calendar()

    responseData = []
    maxEvents = request.args.get('max')

    if maxEvents:
        print('max events: {}'.format(maxEvents))
        responseData = calendar_dao.getMealEvents(max=maxEvents)
    else:
        print('max events: default')
        responseData = calendar_dao.getMealEvents()

    return jsonify(responseData)
