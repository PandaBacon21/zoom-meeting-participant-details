import json
import requests
import os
from dotenv import load_dotenv

from utilities.get_token import token

load_dotenv()

# retrieve the access token
ACCESS_TOKEN = token()

BASE_URL = 'https://api.zoom.us/v2'
HEADERS = {
        'content-type': 'application/json',
        'authorization': f'Bearer {ACCESS_TOKEN}'
    }

def get_users():
    endpoint = '/users'
    full_url = BASE_URL+endpoint
    response = requests.get(url=full_url, headers=HEADERS)
    r_content = json.loads(response.content)
    user_list = []
    for user in r_content['users']: 
        user_list.append({'display_name' : user['display_name'], 'id': user['id']} )
    return user_list

def get_meeting_reports(user_list): 
    users_meetings = {'users': []}
    for user in user_list: 
        endpoint = f"/report/users/{user['id']}/meetings"
        full_url = BASE_URL+endpoint
        params = { 'from': '2024-10-06', 'to': '2024-11-05'}
        response = requests.get(url=full_url, headers=HEADERS, params=params)
        r_content = json.loads(response.content)
        print(f"Retrieving Meetings for user {user['display_name']}")
        users_meetings['users'].append({'user': user['display_name'], 'id': user['id'], 'meetings': r_content['meetings']})
    return users_meetings

def get_meeting_participant_reports(users_meetings): 
    meeting_report = users_meetings
    for user in meeting_report['users']: 
        for meeting in user['meetings']: 
            meeting_uuid = meeting['uuid']
            if (meeting_uuid.startswith('/')) or ('//' in meeting_uuid): 
                meeting_uuid_enconded = meeting_uuid.encode('utf-8')
                meeting_uuid_double_encoded = meeting_uuid_enconded.encode('utf-8')
                meeting_uuid = meeting_uuid_double_encoded
            print(f"Retrieving Participant Details for User: {user['user']}, Meeting UUID: {meeting_uuid}")
            endpoint = f"/report/meetings/{meeting['uuid']}/participants"
            full_url = BASE_URL+endpoint
            response = requests.get(url=full_url, headers=HEADERS)
            r_content = json.loads(response.content)
            meeting['participants_details'] = r_content['participants']
    with open('meeting_details_report.json', 'w') as f:
        print("Creating Meeting Details Report as 'meeting_details_report.json'")
        json.dump(meeting_report, f, indent=4)
    

def main(): 
    user_list = get_users()
    get_meeting_participant_reports(get_meeting_reports(user_list))

if __name__ == '__main__': 
    main()