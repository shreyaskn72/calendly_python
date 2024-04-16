from flask import Flask, redirect, request
import requests

app = Flask(__name__)

# Your Calendly OAuth 2.0 credentials
CLIENT_ID = 'client id'
CLIENT_SECRET = 'client secret'

# Set the redirect URL for your application
REDIRECT_URI = 'http://localhost:8080'  # Change this to your desired redirect URL

AUTHORIZE_URL = 'https://calendly.com/oauth/authorize'
TOKEN_URL = 'https://calendly.com/oauth/token'

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
            return f"Access Token: {access_token}"
        else:
            return "Error occurred while getting access token."
    else:
        return "Error occurred while exchanging authorization code for tokens."

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

if __name__ == '__main__':
    app.run(debug=True)
