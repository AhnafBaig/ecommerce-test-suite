import pytest
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


# ---------------------------------------------------------------------------
# GIVEN
# ---------------------------------------------------------------------------

@given("I am on the login page", target_fixture="login_page")
def navigate_to_login(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    login_page.open()
    return login_page


# ---------------------------------------------------------------------------
# WHEN
# ---------------------------------------------------------------------------

@when(parsers.parse('I enter username "{username}" and password "{password}"'))
def enter_credentials(login_page: LoginPage, username: str, password: str) -> None:
    login_page.enter_username(username)
    login_page.enter_password(password)


@when("I click the login button")
def click_login(login_page: LoginPage) -> None:
    login_page.click_login()


# ---------------------------------------------------------------------------
# THEN
# ---------------------------------------------------------------------------

@then("I should be redirected to the inventory page")
def verify_redirect_to_inventory(page: Page) -> None:
    page.wait_for_url("**/inventory.html")
    assert "inventory.html" in page.url, (
        f"Expected to land on inventory page, but URL is: {page.url}"
    )


@then(parsers.parse('the page title should be "{expected_title}"'))
def verify_page_title(page: Page, expected_title: str) -> None:
    actual = page.inner_text(".title")
    assert actual == expected_title, (
        f"Expected title '{expected_title}', got '{actual}'"
    )


@then("I should see a login error message")
def verify_error_visible(login_page: LoginPage) -> None:
    assert login_page.is_error_visible(), (
        "Expected an error message to be visible on the login page"
    )
