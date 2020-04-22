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

calendar = Calendar()
__CREDENTIALS = calendar.getCredentials()


def getMealEvents():

    service = build('calendar', 'v3', credentials=__CREDENTIALS)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId=__CALENDAR_ID, timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
