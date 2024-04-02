# Calendly Refresh Token to Access Token

This Python script demonstrates how to exchange a refresh token for an access token in Calendly using OAuth 2.0 authentication. It utilizes the Calendly OAuth token endpoint to obtain the access token.

## Prerequisites

- Python 3.x installed on your system.
- `requests` library. Install it using `pip install requests`.

## Usage

1. Replace `"YOUR_CLIENT_ID"` and `"YOUR_CLIENT_SECRET"` in the script with your actual Calendly OAuth client credentials.
2. Run the script.
3. Enter your refresh token when prompted.
4. The script will output the obtained access token.

## Important Note

- This script is provided as a demonstration of how to obtain an access token from a refresh token in Calendly. Ensure you keep your client credentials secure and do not expose them publicly.
- Remember to handle errors and exceptions appropriately in a production environment.