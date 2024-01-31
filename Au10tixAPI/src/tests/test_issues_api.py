from src.api.test_api import get_open_issues_count, get_practice1_issues_count, create_issue, get_total_issues, \
    get_first_issue_title, update_issue_state_to_closed

ISSUE_TITLE = "Test"
issue_number = None


def test_get_open_issues_count(github_headers):
    count = get_open_issues_count(github_headers)
    print(count)


def test_get_practice1_issues_count(github_headers):
    count = get_practice1_issues_count(github_headers)
    print(count)


def test_create_issue(github_headers):
    global issue_number
    result, issue_number = create_issue(github_headers)
    print("Issue creation result:", result)
    assert result



def test_create_issue_and_print_issue_number(github_headers):
    success, issue_number = create_issue(github_headers)
    assert success
    assert issue_number is not None
    print("New issue number:", issue_number)


def test_verify_new_issue_added(github_headers):
    total_issues_before_creation = get_total_issues(github_headers)
    assert total_issues_before_creation != -1

    create_issue(github_headers)
    total_issues_after_creation = get_total_issues(github_headers)
    assert total_issues_after_creation == total_issues_before_creation + 1

    first_issue_title = get_first_issue_title(github_headers)
    assert first_issue_title == ISSUE_TITLE

def test_update_issue_state(github_headers):
    global issue_number
    assert issue_number is not None
    success = update_issue_state_to_closed(issue_number, github_headers)
    assert success


def test_verify_total_issues(github_headers):
    total_issues_before_creation = get_total_issues(github_headers)
    assert total_issues_before_creation != -1

    result, issue_number = create_issue(github_headers)
    assert issue_number is not None

    success = update_issue_state_to_closed(issue_number, github_headers)
    assert success

    total_issues_after_creation = get_total_issues(github_headers)
    assert total_issues_after_creation != -1
    assert total_issues_after_creation == total_issues_before_creation
