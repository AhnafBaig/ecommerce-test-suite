from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object for the SauceDemo inventory/products page."""

    # --- Locators ---
    INVENTORY_CONTAINER = "#inventory_container"
    CART_BADGE = ".shopping_cart_badge"
    CART_ICON = ".shopping_cart_link"
    PAGE_TITLE = ".title"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def is_loaded(self) -> bool:
        return self.page.is_visible(self.INVENTORY_CONTAINER)

    def get_cart_count(self) -> str:
        """Return the cart badge count, or '0' if badge is not present."""
        if self.page.is_visible(self.CART_BADGE):
            return self.page.inner_text(self.CART_BADGE)
        return "0"

    def add_item_to_cart(self, item_name: str) -> None:
        """Click the 'Add to cart' button for a specific product by name."""
        # SauceDemo button IDs follow the pattern: add-to-cart-<slug>
        slug = item_name.lower().replace(" ", "-")
        button_id = f"[data-test='add-to-cart-{slug}']"
        self.page.click(button_id)

    def remove_item_from_cart(self, item_name: str) -> None:
        """Click the 'Remove' button for a specific product by name."""
        slug = item_name.lower().replace(" ", "-")
        button_id = f"[data-test='remove-{slug}']"
        self.page.click(button_id)

    def go_to_cart(self) -> None:
        self.page.click(self.CART_ICON)
