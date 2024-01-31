import pytest

@pytest.fixture(scope="session")
def github_headers():
    headers = {
        "Authorization": "token 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"
    }
    return headers
