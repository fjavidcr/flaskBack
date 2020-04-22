from __future__ import print_function
from googleapiclient.discovery import build
import datetime
from src.handlers.calendar import Calendar
import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('config/config.ini')
__CALENDAR_ID = config['CALENDAR']['ID']

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# service

calendar = Calendar()
__SERVICE = build('calendar', 'v3', credentials=calendar.getCredentials())


def getMealEvents(max=10):

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    print('Getting the upcoming {} events'.format(max))
    events_result = __SERVICE.events().list(calendarId=__CALENDAR_ID, timeMin=now,
                                            maxResults=max, singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
