import requests

# Set your Calendly OAuth client credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Set the redirect URL for your application
redirect_uri = 'https://example.com/oauth/callback'  # Change this to your desired redirect URL

# Set the OAuth endpoints specific to Calendly
authorization_base_url = 'https://auth.calendly.com/oauth/authorize'
token_url = 'https://auth.calendly.com/oauth/token'

# Redirect the user to the authorization URL to initiate the OAuth flow
authorization_url = f'{authorization_base_url}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'

print("Please visit the following URL and authorize the application:")
print(authorization_url)

# After the user authorizes the application, they will be redirected back to the redirect URL
# Extract the authorization code from the redirected URL
authorization_code = input("Enter the authorization code from the redirected URL: ")

# Prepare request parameters for token endpoint to exchange authorization code for tokens
token_data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'code': authorization_code
}

# Make a POST request to the token endpoint to exchange authorization code for tokens
token_response = requests.post(token_url, data=token_data)

# Check if the request was successful
if token_response.ok:
    # Parse the response to get the access token and refresh token
    token_data = token_response.json()
    access_token = token_data.get('access_token')
    refresh_token = token_data.get('refresh_token')

    # Use the access token to make requests to the Calendly API
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Fetch user details
    user_response = requests.get('https://api.calendly.com/users/me', headers=headers)
    if user_response.ok:
        user_data = user_response.json()
        print("User Details:")
        print(user_data)
    else:
        print("Failed to fetch user details. Status code:", user_response.status_code)
else:
    print("Failed to exchange authorization code for tokens. Status code:", token_response.status_code)
