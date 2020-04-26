from flask import Flask, jsonify, Blueprint, request
from src.dao.task import Task

task_bp = Blueprint('task', __name__)

task_dao = None


@task_bp.route('/lists', methods=['GET'])
def lists():
    global task_dao
    if not task_dao:
        task_dao = Task()

    responseData = []
    max = request.args.get('max')

    if max:
        print('max tasks: {}'.format(max))
        responseData = task_dao.getTasksLists(max=max)
    else:
        print('max tasks: default')
        responseData = task_dao.getTasksLists()

    return jsonify(responseData)


@task_bp.route('/mytasks/list', methods=['GET'])
def mytasks_list():
    global task_dao
    if not task_dao:
        task_dao = Task()

    responseData = []
    max = request.args.get('max')

    if max:
        print('max tasks: {}'.format(max))
        responseData = task_dao.getTasksFromList(max=max)
    else:
        print('max tasks: default')
        responseData = task_dao.getTasksFromList()

    return jsonify(responseData)
