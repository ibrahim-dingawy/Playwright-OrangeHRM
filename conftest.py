"""
Pytest configuration and fixtures
"""
import pytest
import json
from pathlib import Path
from datetime import datetime
from playwright.sync_api import Page, BrowserContext, Browser
from config.settings import (
    BASE_URL, BROWSER, HEADLESS, SLOW_MO, TIMEOUT,
    VIEWPORT_WIDTH, VIEWPORT_HEIGHT, SCREENSHOTS_DIR,
    VIDEOS_DIR, TRACES_DIR, TEST_DATA_DIR
)
from utilities.logger import get_logger

logger = get_logger(__name__)


def pytest_configure(config):
    """Create reports directories"""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    TRACES_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context"""
    return {
        **browser_context_args,
        "viewport": {
            "width": VIEWPORT_WIDTH,
            "height": VIEWPORT_HEIGHT,
        },
        "record_video_dir": str(VIDEOS_DIR),
        "record_video_size": {"width": 1280, "height": 720},
    }


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Create a new page for each test"""
    page = context.new_page()

    # Set default timeout
    page.set_default_timeout(TIMEOUT)

    yield page

    page.close()


@pytest.fixture(scope="function")
def mobile_page(playwright) -> Page:
    """
    Create a new page emulating iPhone 14 Pro
    """
    iphone_14_pro = playwright.devices["iPhone 14 Pro"]

    browser = playwright.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO
    )

    context = browser.new_context(
        **iphone_14_pro,
        record_video_dir=str(VIDEOS_DIR),
        record_video_size={"width": 393, "height": 852}  # iPhone 14 Pro actual size
    )

    page = context.new_page()
    page.set_default_timeout(TIMEOUT)

    yield page

    page.close()
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def navigate_to_home(page: Page):
    """Navigate to application home page"""
    logger.info(f"Navigating to: {BASE_URL}")
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    return page


@pytest.fixture(scope="session")
def test_data():
    """Load test data from JSON"""
    test_data_file = TEST_DATA_DIR / "test_data.json"
    with open(test_data_file, 'r') as f:
        data = json.load(f)
    return data


@pytest.fixture(scope="function")
def authenticated_page(page: Page):
    """Create an authenticated page session"""
    from tests.ui.pages.login_page import LoginPage
    from config.settings import ADMIN_USERNAME, ADMIN_PASSWORD

    logger.info("Creating authenticated session")
    page.goto(BASE_URL)

    login_page = LoginPage(page)
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)

    # Wait for dashboard
    page.wait_for_url("**/dashboard/index", timeout=10000)
    logger.info("Authentication successful")

    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get page from test
        page = None
        for fixture_name in item.fixturenames:
            if fixture_name == "page" or fixture_name == "authenticated_page":
                page = item.funcargs.get(fixture_name)
                break

        if page:
            # Take screenshot
            screenshot_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot_path = SCREENSHOTS_DIR / screenshot_name

            try:
                page.screenshot(path=str(screenshot_path), full_page=True)
                logger.info(f"Screenshot saved: {screenshot_path}")
            except Exception as e:
                logger.error(f"Failed to capture screenshot: {e}")


def pytest_html_report_title(report):
    """Customize HTML report title"""
    report.title = "OrangeHRM Test Automation Report"


def pytest_metadata(metadata):
    """Add metadata to HTML report"""
    metadata["Project"] = "OrangeHRM Automation"
    metadata["Base URL"] = BASE_URL
    metadata["Browser"] = BROWSER
    metadata["Headless"] = HEADLESS