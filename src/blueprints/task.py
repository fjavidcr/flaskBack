from flask import Flask, jsonify, Blueprint, request
from src.dao import task

task_bp = Blueprint('task', __name__)


@task_bp.route('/lists', methods=['GET'])
def lists():
    responseData = []

    try:
        max = request.args.get('max')
        print('max tasks: {}'.format(max))
    except:
        print('max tasks: default')

    if max:
        responseData = task.getTasksLists(max=max)
    else:
        responseData = task.getTasksLists()

    return jsonify(responseData)


@task_bp.route('/mytasks/list', methods=['GET'])
def mytasks_list():
    responseData = []

    try:
        max = request.args.get('max')
        print('max tasks: {}'.format(max))
    except:
        print('max tasks: default')

    if max:
        responseData = task.getTasksFromList(max=max)
    else:
        responseData = task.getTasksFromList()

    return jsonify(responseData)
