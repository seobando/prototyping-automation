import requests
from requests.auth import HTTPBasicAuth
import os

JIRA_DOMAIN = os.environ.get("JIRA_DOMAIN")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")
JIRA_USER_EMAIL = os.environ.get("JIRA_USER_EMAIL")


def extract_content(data):
    content_paragraphs = []
    for paragraph in data["content"]:
        for content in paragraph["content"]:
            if "text" in content:
                content_paragraphs.append(content["text"])

    combined_content = " ".join(content_paragraphs)
    return combined_content


def get_user_story(ticket_id):
    url = f"https://{JIRA_DOMAIN}/rest/api/3/issue/{ticket_id}"
    auth = HTTPBasicAuth(JIRA_USER_EMAIL, JIRA_API_TOKEN)
    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, auth=auth)

    ticket_data = response.json()
    data = ticket_data.get("fields", {}).get("description", "Description not found")
    description = extract_content(data)
    return description
