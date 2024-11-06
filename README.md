# Zoom Meeting Participant Details

## Usage
> **Note**
>
> The following sample application is a personal, open-source project shared by the app creator and not an officially supported Zoom Video Communications, Inc. sample application. Zoom Video Communications, Inc., its employees and affiliates are not responsible for the use and maintenance of this application. Please use this sample application for inspiration, exploration and experimentation at your own risk and enjoyment. You may reach out to the app creator and broader Zoom Developer community on https://devforum.zoom.us/ for technical discussion and assistance, but understand there is no service level agreement support for this application. Thank you and happy coding!

You will need to create a ```.env``` file in the root of your project directory and include the following variables: 

```
ACCOUNT_ID = 'YourZoomAccountId'
CLIENT_ID = 'YourZoomClientId'
CLIENT_SECRET = 'YourZoomClientSecret'
DB_LOCATION = 'PathToYourDataBase'
```
I just used a SQLite database for this project but you can use any database that you'd prefer. Or you can simply store the token in memory, but that does result in constantly refreshing the token every time the script is ran.

### Zoom Endpoints and Scopes Used:

```
https://api.zoomus./v2/users
```
To retrieve a list of users on your account
#### Scopes: 
user:read:list_users:admin

[Documentation](https://developers.zoom.us/docs/api/users/#tag/users/GET/users)

```
https://api.zoomus./v2/report/users/{userId}/meetings
```
To retrieve meetings for a specific user within a specific time range - **Time range for the report is limited to a month and the month must fall within the past 6 months**
#### Scopes: 
report:read:user:admin

[Documentation](https://developers.zoom.us/docs/api/meetings/#tag/reports/GET/report/users/{userId}/meetings)

```
https://api.zoomus./v2/report/meetings/{meetingId}/participants
```
To retrieve a participant report of a past meeting with two or more participants, including the host
#### Scopes: 
report:read:list_meeting_participants:admin

[Documentation](https://developers.zoom.us/docs/api/meetings/#tag/reports/GET/report/meetings/{meetingId}/participants)
