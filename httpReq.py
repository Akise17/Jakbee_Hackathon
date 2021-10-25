import json
import requests
import pprint

api_token = 'YzBkM2NjODItNDI3Ny00Mzk0LWIwZDUtYjA1MjQ4MjAxMmNl'
api_url_base = 'https://startspace.kitasiap.id'
basepath = '/api/v1/registration'
headers = {'Content-Type': 'application/json',
           'X-Api-Key': api_token}

body = {
        "sys_id": 1,
        "type": "flexidesk",
        "location": 1,
        "start": "2019-12-21 13:30:00",
        "end": "2019-12-21 23:59:59",
        "profile": {
            "username": "admin",
            "email": "admin@startspace.id",
            "phone": "088888888888"
            }
        }

api_url = '{0}/api/v1/registration'.format(api_url_base)

conn = requests.post(api_url, headers=headers, json=body)
print(conn.status_code)
pprint.pprint(conn.content.decode('utf-8'))
