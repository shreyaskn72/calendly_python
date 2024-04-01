from requests_oauthlib import OAuth2Session

# Set your Calendly OAuth client credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Set the redirect URL for your application
redirect_uri = 'https://example.com/oauth/callback'  # Change this to your desired redirect URL

# Set the OAuth endpoints specific to Calendly
authorization_base_url = 'https://auth.calendly.com/oauth/authorize'
token_url = 'https://auth.calendly.com/oauth/token'

# Create an OAuth2Session object with your client credentials
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

# Obtain the authorization URL
authorization_url, state = oauth.authorization_url(authorization_base_url)

# Print the authorization URL for the user to visit and authorize the application
print("Please visit the following URL and authorize the application:")
print(authorization_url)

# After the user authorizes the application, they will be redirected back to the redirect URL
# Extract the authorization response from the redirected URL
redirect_response = input("Paste the full URL you were redirected to: ")

# Parse the authorization response to extract the authorization code
authorization_response = oauth.parse_authorization_response(redirect_response)

# Exchange the authorization code for tokens
token = oauth.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret)

# Access token and refresh token are available in the token dictionary
access_token = token['access_token']
refresh_token = token['refresh_token']

# Now you can use the access token and refresh token to make requests to the Calendly API
# For example, you can fetch user details
user_response = oauth.get('https://api.calendly.com/users/me')
if user_response.ok:
    user_data = user_response.json()
    print("User Details:")
    print(user_data)
else:
    print("Failed to fetch user details. Status code:", user_response.status_code)
