# Calendly OAuth Python Example

This Python script demonstrates how to interact with Calendly OAuth application to obtain an access token using client credentials grant type and fetch user details from the Calendly API.

## Prerequisites

Before running the script, make sure you have the following:

- Calendly OAuth client credentials (client ID and client secret)
- Python installed on your system
- `requests_oauthlib` library installed (`pip install requests_oauthlib`)

## Usage

1. Replace `your_client_id` and `your_client_secret` with your Calendly OAuth application's client ID and client secret respectively in the `calendly_oauth.py` script.
2. Run the script using Python:

   ```bash
   python calendly_oauth.py
   ```
## Script Explanation

- The script uses the requests_oauthlib library to handle the OAuth authentication process.
- It sets up an OAuth2 session with Calendly using client credentials grant type.
- The script fetches an access token from Calendly's OAuth server using the provided client ID and client secret.
- Once the access token is obtained, it makes a request to fetch user details from the Calendly API.
- The fetched user details are printed to the console.

