from flask import Flask, redirect, request
import requests

app = Flask(__name__)

# Your Calendly OAuth 2.0 credentials
CLIENT_ID = 'client_id'
CLIENT_SECRET = 'client_secret'

# Set the redirect URL for your application
REDIRECT_URI = 'http://localhost:8080/callback'  # Change this to your desired redirect URL

AUTHORIZE_URL = 'https://calendly.com/oauth/authorize'
TOKEN_URL = 'https://calendly.com/oauth/token'


def get_access_token(refresh_token):
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=payload)
    if response.status_code == 200:
        output = response.json()
        print(output)
        return output.get('access_token')
    else:
        print("Error occurred while getting access token:")
        print("Status code:", response.status_code)
        print("Response:", response.json())
        return None

def list_meeting_types(access_token, organization):
    url = 'https://api.calendly.com/event_types'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    params = {
        'organization': organization
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
        for event_type in data['collection']:
            print(event_type)
            print(event_type['name'])
    else:
        print("Error occurred while fetching meeting types:")
        print("Status code:", response.status_code)
        print("Response:", response.json())

    output_event_types = response.json()

    return output_event_types


def user_me(access_token):
    # Use the access token to make requests to the Calendly API
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Fetch user details
    user_response = requests.get('https://api.calendly.com/users/me', headers=headers)

    user_data = user_response.json()

    print("user_data")

    print(user_data)

    return user_data



@app.route('/')
def home():
    return redirect(AUTHORIZE_URL + '?response_type=code&client_id=' + CLIENT_ID + '&redirect_uri=' + REDIRECT_URI)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=payload)
    if response.status_code == 200:
        data = response.json()
        print(data)
        refresh_token = data['refresh_token']
        access_token = get_access_token(refresh_token)
        if access_token:
            return data
        else:
            return "Error occurred while getting access token."
    else:
        return "Error occurred while exchanging authorization code for tokens."

@app.route('/get_users_data', methods=["POST"])
def get_users_data():
    access_token = request.json['access_token']
    user_data = user_me(access_token)
    return user_data

@app.route("/get_event_types", methods=["POST"])
def get_event_types():
    access_token = request.json['access_token']
    user_data = user_me(access_token)
    print("type of user data is")
    print(type(user_data))
    print(user_data)
    current_organization = user_data["resource"]["current_organization"]

    output_event_types = list_meeting_types(access_token, current_organization)

    #event_type_list = []
    event_type_dict = {}

    for event_type in output_event_types['collection']:
        event_type_dict[event_type['name']] = [event_type['uri'],event_type['scheduling_url']]
        # event_type_list.append(event_type['name'])

    return event_type_dict





if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
    #app.run(debug=True)
