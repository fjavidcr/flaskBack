from __future__ import print_function
from googleapiclient.discovery import build
import datetime
from src.handlers import googleApi
import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('config/config.ini')
__CALENDAR_ID = config['CALENDAR']['ID']

# service
__SERVICE = googleApi.getService(apiName='calendar', apiVersion='v3')


def getMealEvents(max='10'):

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    print('Getting the upcoming {} meal events'.format(max))
    events_result = __SERVICE.events().list(calendarId=__CALENDAR_ID, timeMin=now,
                                            maxResults=max, singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return 404
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])
    return events
