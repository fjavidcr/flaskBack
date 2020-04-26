from __future__ import print_function
from googleapiclient.discovery import build
import datetime
from src.handlers import googleApi
import configparser

# CONFIG
config = configparser.ConfigParser()


class Task():

    __TASK_ID = None
    __SERVICE = None

    def __init__(self):

        config.read('config/config.ini')
        self.__TASK_ID = config['TASK']['ID']
        # service
        self.__SERVICE = googleApi.getService(apiName='tasks', apiVersion='v1')

    def getTasksLists(self, max='10'):

        print('Getting the upcoming {} tasks'.format(max))
        results = self.__SERVICE.tasklists().list(maxResults=max).execute()
        items = results.get('items', [])

        if not items:
            print('No task lists found.')
        else:
            print('Task lists:')
            for item in items:
                print(u'{0} ({1})'.format(item['title'], item['id']))

        return items

    def getTasksFromList(self, max='10'):
        print('Getting the upcoming {} tasks'.format(max))
        results = self.__SERVICE.tasks().list(tasklist=self.__TASK_ID, showCompleted=False, dueMin=None, dueMax=None,
                                              showDeleted=False, maxResults=max, showHidden=False).execute()
        items = results.get('items', [])

        if not items:
            print('No task lists found.')
            return 404
        else:
            print('Tasks list:')
            for item in items:
                print(u'{0} ({1})'.format(item['title'], item['id']))

        return items
