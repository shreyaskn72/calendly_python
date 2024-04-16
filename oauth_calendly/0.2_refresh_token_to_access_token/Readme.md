# Calendly OAuth 2.0 Authorization Code Flow Example using cURL

This guide demonstrates how to manually perform the OAuth 2.0 Authorization Code Flow with Calendly's API using cURL commands.

## Prerequisites

Before using these cURL commands, you need to have:

- cURL installed on your system.
- Calendly API credentials (Client ID and Client Secret). You can obtain these by registering your application with Calendly.

## Steps

### 1. Get Authorization Code

Use the following cURL command to initiate the authorization process and obtain the authorization code:

```bash
curl -X GET "https://calendly.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:5000/callback"
```

Replace YOUR_CLIENT_ID with your actual Calendly OAuth client ID.

### 2. Exchange Authorization Code for Refresh Token
After obtaining the authorization code from Step 1, use the following cURL command to exchange it for a refresh token:
```bash
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=authorization_code&code=AUTHORIZATION_CODE&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&redirect_uri=http://localhost:5000/callback" "https://calendly.com/oauth/token"
```

Replace AUTHORIZATION_CODE with the obtained authorization code, YOUR_CLIENT_ID with your actual Calendly OAuth client ID, and YOUR_CLIENT_SECRET with your actual Calendly OAuth client secret.

### 3. Exchange Refresh Token for Access Token (optional)
If needed, you can exchange the obtained refresh token for an access token using the following cURL command:
```bash
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token=REFRESH_TOKEN&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET" "https://calendly.com/oauth/token"
```