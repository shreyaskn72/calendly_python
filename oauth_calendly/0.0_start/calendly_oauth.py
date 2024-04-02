from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

# Set your Calendly OAuth client credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Set the OAuth endpoints specific to Calendly
authorization_base_url = 'https://auth.calendly.com/oauth/authorize'
token_url = 'https://auth.calendly.com/oauth/token'

# Create an OAuth2Session object using BackendApplicationClient
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Fetch access token using client credentials
token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

# Now, you have the access token to make requests to the Calendly API
# For example, you can fetch user details
user_response = oauth.get('https://api.calendly.com/users/me')
if user_response.status_code == 200:
    user_data = user_response.json()
    print("User Details:")
    print(user_data)
else:
    print("Failed to fetch user details. Status code:", user_response.status_code)
