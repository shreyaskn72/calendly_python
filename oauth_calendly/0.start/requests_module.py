import requests

# Set your Calendly OAuth client credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Set the redirect URL for your application
redirect_uri = 'https://example.com/oauth/callback'  # Change this to your desired redirect URL

# Set the OAuth endpoints specific to Calendly
authorization_base_url = 'https://auth.calendly.com/oauth/authorize'
token_url = 'https://auth.calendly.com/oauth/token'

# Prepare request parameters for token endpoint
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# Make a POST request to the token endpoint to obtain an access token
token_response = requests.post(token_url, data=token_data)

# Check if the request was successful
if token_response.ok:
    # Parse the response to get the access token
    access_token = token_response.json().get('access_token')

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
    print("Failed to obtain access token. Status code:", token_response.status_code)
