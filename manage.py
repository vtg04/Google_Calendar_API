from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account key file
SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'

# Scopes required by the API
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('calendar', 'v3', credentials=creds)

# Managing Calendar Events

event_id = 'eventId'
event = service.events().get(calendarId='primary', eventId=event_id).execute()

event['summary'] = 'Updated Meeting with Bob'
updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()

print('Event updated: %s' % (updated_event.get('htmlLink')))
