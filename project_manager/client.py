import requests
from requests.auth import HTTPBasicAuth
import os

JIRA_DOMAIN = os.environ.get("JIRA_DOMAIN")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")
JIRA_USER_EMAIL = os.environ.get("JIRA_USER_EMAIL")

def get_ticket_description(ticket_id):
    url = f"https://{JIRA_DOMAIN}/rest/api/3/issue/{ticket_id}"
    auth = HTTPBasicAuth(JIRA_USER_EMAIL, JIRA_API_TOKEN)
    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    # Parse the JSON response and return the description
    ticket_data = response.json()
    return ticket_data.get('fields', {}).get('description', 'Description not found')