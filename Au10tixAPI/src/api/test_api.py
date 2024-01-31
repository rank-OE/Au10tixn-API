import pytest
import requests
import json

repository = "topq-practice/api-practice"
token = "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"
headers = {"Authorization": f"token {token}"}
repository_owner = "topq-practice"
repository_name = "api-practice"
ISSUE_TITLE = "Test"


def get_open_issues_count(headers):
    url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/issues?state=open"
    response = requests.get(url, headers=headers)
    issues = response.json()
    return len(issues)


def get_practice1_issues_count(headers):
    url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/issues?labels=practice1"
    response = requests.get(url, headers=headers)
    issues = response.json()
    return len(issues)


def create_issue(headers):
    breakpoint()
    url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/issues"
    payload = {
        "title": ISSUE_TITLE,
        "body": "This issue was created via REST API from Python by Ran k",
        "labels": ["practice1"],
        "assignees": ["topq-practice"]
    }

    print("URL:", url)
    print("Payload:", payload)
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        issue_number = response.json().get('number')
        return True, issue_number
    else:
        return False, None


def get_total_issues(headers):
    repository_owner = "topq-practice"
    repository_name = "api-practice"
    url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/issues"

    total_issues = 0
    page = 1
    while True:
        params = {"page": page}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            issues_on_page = len(response.json())
            total_issues += issues_on_page
            if issues_on_page == 0:
                break
            page += 1
        else:
            total_issues = -1
            break

    return total_issues


def get_first_issue_title(headers):
    url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/issues"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        first_issue_title = response.json()[0]['title']
        return first_issue_title
    else:
        return None

def update_issue_state_to_closed(issue_number, headers):
    url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/issues/{issue_number}"
    data = {
        "state": "closed",
        "state_reason": "not_planned"
    }
    response = requests.patch(url, headers=headers, json=data)

    return response.status_code == 200



