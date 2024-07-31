# Google Calendar API Automation

This project demonstrates how to integrate the Google Calendar API into your application using Python. It covers setting up the API credentials, authenticating users, and creating a calendar event in Indian Standard Time (IST).

## Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/Google_Calendar_API.git
```

### Navigate to the Project Directory

```bash
cd Google_Calendar_API
```

### Install Required Libraries

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Set Environment Variable
Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of your service account key:

```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\service-account-file.json
```

## Usage

### Create a Calendar Event
Run the Python script create.py to create an event:

```bash
python create.py
```

### Retrieving Calendar Events
Run the script to retrieve events:

```bash
python retrieve.py
```

### Managing Calendar Events
Run the script to manage events:

```bash
python manage.py
```
