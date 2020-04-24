from __future__ import print_function
from googleapiclient.discovery import build
import datetime
from src.handlers import googleApi
import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('config/config.ini')
__TASK_ID = config['TASK']['ID']

# service
__SERVICE = googleApi.getService(apiName='tasks', apiVersion='v1')


def getTasksLists(max='10'):

    print('Getting the upcoming {} tasks'.format(max))
    results = __SERVICE.tasklists().list(maxResults=max).execute()
    items = results.get('items', [])

    if not items:
        print('No task lists found.')
    else:
        print('Task lists:')
        for item in items:
            print(u'{0} ({1})'.format(item['title'], item['id']))

    return items


def getTasksFromList(max='10'):
    print('Getting the upcoming {} tasks'.format(max))
    results = __SERVICE.tasks().list(tasklist=__TASK_ID, showCompleted=False, dueMin=None, dueMax=None,
                                     showDeleted=False, maxResults=max, showHidden=False).execute()
    items = results.get('items', [])

    if not items:
        print('No task lists found.')
        return 404
    else:
        print('Task lists:')
        for item in items:
            print(u'{0} ({1})'.format(item['title'], item['id']))

    return items
