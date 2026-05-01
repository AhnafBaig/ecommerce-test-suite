from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the SauceDemo login page.

    Encapsulates all selectors and actions related to authentication,
    following the Page Object Model (POM) pattern.
    """

    # --- Locators ---
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> None:
        """Navigate directly to the login page."""
        self.navigate()

    def enter_username(self, username: str) -> None:
        self.page.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        self.page.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Full login action: fill credentials and submit."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        return self.page.inner_text(self.ERROR_MESSAGE)

    def is_error_visible(self) -> bool:
        return self.page.is_visible(self.ERROR_MESSAGE)
