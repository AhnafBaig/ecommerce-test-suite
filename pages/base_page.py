from playwright.sync_api import Page
from utils.config import Config


class BasePage:
    """Base class for all page objects. Holds the Playwright page instance
    and common helper methods shared across all pages."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = Config.UI_BASE_URL

    def navigate(self, path: str = "") -> None:
        """Navigate to a URL relative to the base URL."""
        self.page.goto(f"{self.base_url}{path}")

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url

    def wait_for_url(self, url_fragment: str) -> None:
        self.page.wait_for_url(f"**{url_fragment}**")
