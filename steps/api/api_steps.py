import json
import pytest
import requests
from pytest_bdd import given, when, then, parsers

from utils.config import Config


# ---------------------------------------------------------------------------
# Shared context fixture — carries response between steps within a scenario
# ---------------------------------------------------------------------------

@pytest.fixture
def api_context() -> dict:
    """Shared mutable dict for passing state (response) between steps."""
    return {}


# ---------------------------------------------------------------------------
# WHEN
# ---------------------------------------------------------------------------

@when(parsers.parse("I send a GET request to \"{endpoint}\""))
def send_get_request(api_context: dict, endpoint: str) -> None:
    url = f"{Config.API_BASE_URL}{endpoint}"
    response = requests.get(url, timeout=10)
    api_context["response"] = response


@when(parsers.parse("I send a POST request to \"{endpoint}\" with JSON body:\n{body}"))
def send_post_request(api_context: dict, endpoint: str, body: str) -> None:
    url = f"{Config.API_BASE_URL}{endpoint}"
    payload = json.loads(body.strip())
    response = requests.post(url, json=payload, timeout=10)
    api_context["response"] = response


# ---------------------------------------------------------------------------
# THEN
# ---------------------------------------------------------------------------

@then(parsers.parse("the response status code should be {status_code:d}"))
def verify_status_code(api_context: dict, status_code: int) -> None:
    actual = api_context["response"].status_code
    assert actual == status_code, (
        f"Expected HTTP {status_code}, got {actual}. "
        f"Body: {api_context['response'].text[:200]}"
    )


@then("the response should be a non-empty list")
def verify_non_empty_list(api_context: dict) -> None:
    data = api_context["response"].json()
    assert isinstance(data, list), f"Expected a list, got {type(data)}"
    assert len(data) > 0, "Expected a non-empty list, but got an empty list"


@then(parsers.parse("the response body field \"{field}\" should equal \"{expected_value}\""))
def verify_body_field(api_context: dict, field: str, expected_value: str) -> None:
    data = api_context["response"].json()
    assert field in data, f"Field '{field}' not found in response body: {data}"
    actual = str(data[field])
    assert actual == expected_value, (
        f"Field '{field}': expected '{expected_value}', got '{actual}'"
    )


@then(parsers.parse("the response content type should contain \"{expected_type}\""))
def verify_content_type(api_context: dict, expected_type: str) -> None:
    content_type = api_context["response"].headers.get("Content-Type", "")
    assert expected_type in content_type, (
        f"Expected Content-Type to contain '{expected_type}', got '{content_type}'"
    )
