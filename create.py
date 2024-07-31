from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account key file
SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'

# Scopes required by the API
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('calendar', 'v3', credentials=creds)

# Creating Calendar Events

event = {
    'summary': 'Meeting with HR',
    'start': {
        'dateTime': '2024-08-01T14:00:00+05:30',
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': '2024-08-01T15:00:00+05:30',
        'timeZone': 'Asia/Kolkata',
    },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))

