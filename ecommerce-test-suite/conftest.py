"""
Root conftest.py
----------------
Registers all step definition modules so pytest-bdd discovers them globally,
and provides the Playwright browser/page fixtures used across UI tests.
"""
import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from utils.config import Config

# ---------------------------------------------------------------------------
# Import step modules so pytest-bdd discovers them automatically
# ---------------------------------------------------------------------------
from steps.ui import login_steps, cart_steps       # noqa: F401
from steps.api import api_steps                     # noqa: F401


# ---------------------------------------------------------------------------
# Playwright fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def browser():
    """Launch a single browser instance for the entire test session."""
    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=Config.HEADLESS,
            slow_mo=Config.SLOW_MO,
        )
        yield browser
        browser.close()


@pytest.fixture
def context(browser: Browser):
    """Create a fresh browser context (isolated cookies/storage) per test."""
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 720},
    )
    ctx.set_default_timeout(Config.TIMEOUT)
    yield ctx
    ctx.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    """Open a new page in the browser context for each test."""
    pg = context.new_page()
    yield pg
    pg.close()
