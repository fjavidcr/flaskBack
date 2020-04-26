from __future__ import print_function
from googleapiclient.discovery import build
import datetime
from src.handlers import googleApi
import configparser

# CONFIG
config = configparser.ConfigParser()


class Calendar():

    __CALENDAR_ID = None
    __SERVICE = None
    _now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    def __init__(self):

        config.read('config/config.ini')
        self.__CALENDAR_ID = config['CALENDAR']['ID']
        # service
        self.__SERVICE = googleApi.getService(
            apiName='calendar', apiVersion='v3')

    def getMealEvents(self, max='10'):

        print('Getting the upcoming {} meal events'.format(max))
        events_result = self.__SERVICE.events().list(calendarId=self.__CALENDAR_ID, timeMin=self._now,
                                                     maxResults=max, singleEvents=True,
                                                     orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            return 404
        # for event in events:
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(start, event['summary'])
        return events
