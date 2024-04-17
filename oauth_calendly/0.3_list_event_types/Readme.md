# Calendly OAuth 2.0 Authorization Code Flow Example with Backend Parsing

This is a simple Flask application demonstrating the OAuth 2.0 Authorization Code Flow with Calendly's API. It allows you to obtain an access token by redirecting the user to Calendly's authorization endpoint and parsing the authorization code from the redirect URL in the backend.

## Prerequisites

Before running this application, you need to have:

- Python installed on your system.
- Calendly API credentials (Client ID and Client Secret). You can obtain these by registering your application with Calendly.

## Steps
### step 1. Getting the access token and refresh token from authorization code

- Go to the below url with web browser like google chrome, microsoft edge, firefox <br />
        <http://localhost:8080>
- It will take to the calendly login page. Please login to calendly
- Then it will get a code and redirects to redirected url configured. In our case redirected url is <br />
http://localhost:8080/callback
- Upon calling this url it will give access token, refresh token, etc as the response
- Example response is given below:
```json
{
  "access_token": "access token field output",
  "created_at": 1713335606,
  "expires_in": 7200,
  "organization": "https://api.calendly.com/organizations/<id>",
  "owner": "https://api.calendly.com/users/<id>",
  "refresh_token": "refesh token field output",
  "scope": "default",
  "token_type": "Bearer"
}
```
### step 2. Fetching user's data based on access token
Input the access token obtained in step 1 as payload json and call /get_users_data endpoint as per the curl command
```curl
curl --location 'http://localhost:8080/get_users_data' \
--header 'Content-Type: application/json' \
--data '{
    "access_token": "access token obtained in step 1"
}'
```

### step 3. Fetching meeting types based on access token
Input the access token obtained in step 1 as payload json and call /get_event_types endpoint as per the curl command below
```curl
curl --location 'http://localhost:8080/get_event_types' \
--header 'Content-Type: application/json' \
--data '{
    "access_token": "access token obtained in step 1"
}'
```
#### Note:
step 1 should be opened in web browsers like google chrome, microsoft edge, firefox, etc. Refer to postman collection attached for step 2 and step 3.