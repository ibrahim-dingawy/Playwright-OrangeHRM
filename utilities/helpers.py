"""
Helper utilities for common operations
"""
import time
import random
import string
from datetime import datetime, timedelta
from typing import Optional
from playwright.sync_api import Page, expect
from utilities.logger import get_logger

logger = get_logger(__name__)


def wait_for_element(page: Page, selector: str, timeout: int = 10000, state: str = "visible"):
    """
    Wait for element with timeout

    Args:
        page: Playwright page
        selector: Element selector
        timeout: Timeout in milliseconds
        state: Element state to wait for (visible, attached, detached, hidden)
    """
    try:
        page.wait_for_selector(selector, timeout=timeout, state=state)
        logger.debug(f"Element found: {selector}")
        return True
    except Exception as e:
        logger.error(f"Element not found: {selector} - {e}")
        return False


def safe_click(page: Page, selector: str, timeout: int = 5000):
    """
    Safely click element with retry

    Args:
        page: Playwright page
        selector: Element selector
        timeout: Timeout in milliseconds
    """
    try:
        element = page.locator(selector)
        element.wait_for(timeout=timeout, state="visible")
        element.click()
        logger.debug(f"Clicked: {selector}")
        return True
    except Exception as e:
        logger.error(f"Failed to click: {selector} - {e}")
        return False


def safe_fill(page: Page, selector: str, text: str, timeout: int = 5000):
    """
    Safely fill input field

    Args:
        page: Playwright page
        selector: Element selector
        text: Text to fill
        timeout: Timeout in milliseconds
    """
    try:
        element = page.locator(selector)
        element.wait_for(timeout=timeout, state="visible")
        element.clear()
        element.fill(text)
        logger.debug(f"Filled '{selector}' with: {text}")
        return True
    except Exception as e:
        logger.error(f"Failed to fill: {selector} - {e}")
        return False


def get_text(page: Page, selector: str, timeout: int = 5000) -> Optional[str]:
    """
    Get text from element

    Args:
        page: Playwright page
        selector: Element selector
        timeout: Timeout in milliseconds

    Returns:
        Element text or None
    """
    try:
        element = page.locator(selector)
        element.wait_for(timeout=timeout, state="visible")
        text = element.inner_text()
        logger.debug(f"Got text from '{selector}': {text}")
        return text
    except Exception as e:
        logger.error(f"Failed to get text from: {selector} - {e}")
        return None


def is_element_visible(page: Page, selector: str, timeout: int = 5000) -> bool:
    """
    Check if element is visible

    Args:
        page: Playwright page
        selector: Element selector
        timeout: Timeout in milliseconds

    Returns:
        True if visible, False otherwise
    """
    try:
        element = page.locator(selector)
        element.wait_for(timeout=timeout, state="visible")
        return element.is_visible()
    except:
        return False


def scroll_to_element(page: Page, selector: str):
    """
    Scroll element into view

    Args:
        page: Playwright page
        selector: Element selector
    """
    try:
        element = page.locator(selector)
        element.scroll_into_view_if_needed()
        logger.debug(f"Scrolled to: {selector}")
    except Exception as e:
        logger.error(f"Failed to scroll to: {selector} - {e}")


def take_screenshot(page: Page, name: str):
    """
    Take screenshot with custom name

    Args:
        page: Playwright page
        name: Screenshot name
    """
    from config.settings import SCREENSHOTS_DIR

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{name}_{timestamp}.png"
    path = SCREENSHOTS_DIR / filename

    try:
        page.screenshot(path=str(path), full_page=True)
        logger.info(f"Screenshot saved: {path}")
    except Exception as e:
        logger.error(f"Failed to take screenshot: {e}")


def generate_random_string(length: int = 8) -> str:
    """Generate random string"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_email() -> str:
    """Generate random email"""
    return f"test_{generate_random_string(8)}@example.com"


def get_current_timestamp() -> str:
    """Get current timestamp as string"""
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def wait(seconds: int):
    """Wait for specified seconds"""
    logger.debug(f"Waiting for {seconds} seconds")
    time.sleep(seconds)


def assert_url_contains(page: Page, expected: str):
    """Assert URL contains expected text"""
    current_url = page.url
    assert expected in current_url, f"Expected '{expected}' in URL, but got: {current_url}"
    logger.info(f"URL assertion passed: '{expected}' found in {current_url}")


def assert_text_visible(page: Page, text: str):
    """Assert text is visible on page"""
    expect(page.locator(f"text={text}")).to_be_visible()
    logger.info(f"Text assertion passed: '{text}' is visible")