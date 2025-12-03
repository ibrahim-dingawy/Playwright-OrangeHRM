"""
Base Page Object - Parent class for all page objects
"""
from playwright.sync_api import Page, expect
from utilities.logger import get_logger
from config.settings import TIMEOUT

logger = get_logger(__name__)


class BasePage:
    """Base Page Object with common methods"""

    def __init__(self, page: Page):
        self.page = page
        self.timeout = TIMEOUT

    def navigate_to(self, url: str):
        """Navigate to URL"""
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def click(self, selector: str):
        """Click element"""
        logger.debug(f"Clicking: {selector}")
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        """Fill input field"""
        logger.debug(f"Filling '{selector}' with: {text}")
        self.page.locator(selector).fill(text)

    def clear_and_fill(self, selector: str, text: str):
        """Clear and fill input field"""
        logger.debug(f"Clearing and filling '{selector}' with: {text}")
        element = self.page.locator(selector)
        element.clear()
        element.fill(text)

    def get_text(self, selector: str) -> str:
        """Get text from element"""
        text = self.page.locator(selector).inner_text()
        logger.debug(f"Got text from '{selector}': {text}")
        return text

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        """Check if element is visible"""
        try:
            self.page.locator(selector).wait_for(timeout=timeout, state="visible")
            return True
        except:
            return False

    def is_enabled(self, selector: str) -> bool:
        """Check if element is enabled"""
        return self.page.locator(selector).is_enabled()

    def wait_for_element(self, selector: str, state: str = "visible", timeout: int = None):
        """Wait for element with specified state"""
        if timeout is None:
            timeout = self.timeout
        logger.debug(f"Waiting for '{selector}' to be {state}")
        self.page.locator(selector).wait_for(timeout=timeout, state=state)

    def wait_for_url(self, url_pattern: str, timeout: int = None):
        """Wait for URL to match pattern"""
        if timeout is None:
            timeout = self.timeout
        logger.debug(f"Waiting for URL: {url_pattern}")
        self.page.wait_for_url(url_pattern, timeout=timeout)

    def get_current_url(self) -> str:
        """Get current page URL"""
        return self.page.url

    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()

    def press_key(self, selector: str, key: str):
        """Press key on element"""
        logger.debug(f"Pressing {key} on: {selector}")
        self.page.locator(selector).press(key)

    def hover(self, selector: str):
        """Hover over element"""
        logger.debug(f"Hovering: {selector}")
        self.page.locator(selector).hover()

    def select_dropdown(self, selector: str, value: str):
        """Select dropdown option"""
        logger.debug(f"Selecting '{value}' from: {selector}")
        self.page.locator(selector).select_option(value)

    def check_checkbox(self, selector: str):
        """Check checkbox"""
        logger.debug(f"Checking checkbox: {selector}")
        self.page.locator(selector).check()

    def uncheck_checkbox(self, selector: str):
        """Uncheck checkbox"""
        logger.debug(f"Unchecking checkbox: {selector}")
        self.page.locator(selector).uncheck()

    def scroll_to_element(self, selector: str):
        """Scroll element into view"""
        logger.debug(f"Scrolling to: {selector}")
        self.page.locator(selector).scroll_into_view_if_needed()

    def take_screenshot(self, name: str):
        """Take screenshot"""
        from config.settings import SCREENSHOTS_DIR
        from datetime import datetime

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        path = SCREENSHOTS_DIR / f"{name}_{timestamp}.png"
        self.page.screenshot(path=str(path), full_page=True)
        logger.info(f"Screenshot saved: {path}")

    def wait_for_loading_to_disappear(self, timeout: int = 10000):
        """Wait for loading spinner to disappear"""
        try:
            self.page.wait_for_selector(".oxd-loading-spinner", state="hidden", timeout=timeout)
            logger.debug("Loading spinner disappeared")
        except:
            logger.debug("No loading spinner found")

    # Assertion helpers
    def assert_element_visible(self, selector: str, message: str = None):
        """Assert element is visible"""
        if message is None:
            message = f"Element should be visible: {selector}"
        expect(self.page.locator(selector)).to_be_visible()
        logger.info(f"Assertion passed: {message}")

    def assert_element_hidden(self, selector: str, message: str = None):
        """Assert element is hidden"""
        if message is None:
            message = f"Element should be hidden: {selector}"
        expect(self.page.locator(selector)).to_be_hidden()
        logger.info(f"Assertion passed: {message}")

    def assert_text_equals(self, selector: str, expected_text: str):
        """Assert element text equals expected"""
        expect(self.page.locator(selector)).to_have_text(expected_text)
        logger.info(f"Assertion passed: Text equals '{expected_text}'")

    def assert_text_contains(self, selector: str, expected_text: str):
        """Assert element text contains expected"""
        expect(self.page.locator(selector)).to_contain_text(expected_text)
        logger.info(f"Assertion passed: Text contains '{expected_text}'")

    def assert_url_contains(self, expected: str):
        """Assert URL contains expected text"""
        current_url = self.get_current_url()
        assert expected in current_url, f"Expected '{expected}' in URL, got: {current_url}"
        logger.info(f"Assertion passed: URL contains '{expected}'")

    def assert_count(self, selector: str, expected_count: int):
        """Assert element count"""
        expect(self.page.locator(selector)).to_have_count(expected_count)
        logger.info(f"Assertion passed: Count is {expected_count}")