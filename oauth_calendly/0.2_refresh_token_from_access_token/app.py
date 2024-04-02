import requests

def get_access_token(refresh_token):
    # Calendly OAuth token endpoint
    token_url = "https://api.calendly.com/oauth/token"

    # Calendly OAuth client credentials
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"

    # Request payload
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    # Send POST request to obtain access token
    response = requests.post(token_url, data=data)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        token_data = response.json()
        access_token = token_data.get('access_token')
        return access_token
    else:
        print("Error:", response.status_code)
        print(response.text)
        return None

def main():
    # Input refresh token from the user
    refresh_token = input("Enter your refresh token: ")

    # Get access token
    access_token = get_access_token(refresh_token)
    if access_token:
        print("Access token:", access_token)
    else:
        print("Failed to retrieve access token.")

if __name__ == "__main__":
    main()
