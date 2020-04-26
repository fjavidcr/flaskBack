from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import configparser

# CONFIG
config = configparser.ConfigParser()
__GOOGLE_CREDENTIALS = None
__SERVICE = None

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/tasks.readonly'
]


def __getCredentials():
    print('\n\t+ Getting Google Credentials...\n')
    global config, __GOOGLE_CREDENTIALS

    if not __GOOGLE_CREDENTIALS:
        config.read('config/config.ini')
        __GOOGLE_CREDENTIALS = config['GOOGLE']['CREDENTIALS']

    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                __GOOGLE_CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def getService(apiName='', apiVersion=''):
    __SERVICE = build(apiName, apiVersion,
                      credentials=__getCredentials())
    return __SERVICE

# class GoogleAPI:
#     def __init__(self):
#         """Shows basic usage of the Google Calendar API.
#         Prints the start and name of the next 10 events on the user's calendar.
#         """
#         creds = None
#         # The file token.pickle stores the user's access and refresh tokens, and is
#         # created automatically when the authorization flow completes for the first
#         # time.
#         if os.path.exists('token.pickle'):
#             with open('token.pickle', 'rb') as token:
#                 creds = pickle.load(token)
#         # If there are no (valid) credentials available, let the user log in.
#         if not creds or not creds.valid:
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:
#                 flow = InstalledAppFlow.from_client_secrets_file(
#                     __GOOGLE_CREDENTIALS, SCOPES)
#                 creds = flow.run_local_server(port=0)
#             # Save the credentials for the next run
#             with open('token.pickle', 'wb') as token:
#                 pickle.dump(creds, token)

#         self.__credentials = creds

#     def getCredentials(self):
#         return self.__credentials
