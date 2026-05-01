from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import Config


# ---------------------------------------------------------------------------
# GIVEN
# ---------------------------------------------------------------------------

@given("I am logged in as a standard user", target_fixture="inventory_page")
def login_as_standard_user(page: Page) -> InventoryPage:
    """Background step: log in before each cart scenario."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(Config.STANDARD_USER, Config.PASSWORD)
    page.wait_for_url("**/inventory.html")
    return InventoryPage(page)


# ---------------------------------------------------------------------------
# WHEN
# ---------------------------------------------------------------------------

@when(parsers.parse('I add "{item_name}" to the cart'))
def add_item_to_cart(inventory_page: InventoryPage, item_name: str) -> None:
    inventory_page.add_item_to_cart(item_name)


@when(parsers.parse('I remove "{item_name}" from the cart'))
def remove_item_from_cart(inventory_page: InventoryPage, item_name: str) -> None:
    inventory_page.remove_item_from_cart(item_name)


@when("I navigate to the cart page")
def navigate_to_cart(page: Page) -> None:
    page.click(".shopping_cart_link")


# ---------------------------------------------------------------------------
# THEN
# ---------------------------------------------------------------------------

@then(parsers.parse('the cart count should be "{expected_count}"'))
def verify_cart_count(inventory_page: InventoryPage, expected_count: str) -> None:
    actual = inventory_page.get_cart_count()
    assert actual == expected_count, (
        f"Expected cart count '{expected_count}', got '{actual}'"
    )


@then(parsers.parse('I should see "{item_name}" in the cart'))
def verify_item_in_cart(page: Page, item_name: str) -> None:
    cart_page = CartPage(page)
    items_in_cart = cart_page.get_item_names()
    assert item_name in items_in_cart, (
        f"Expected '{item_name}' to be in cart, but found: {items_in_cart}"
    )
