"""
Login Tests
"""
import pytest
from playwright.sync_api import Page
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.dashboard_page import DashboardPage
from config.settings import ADMIN_USERNAME, ADMIN_PASSWORD
from utilities.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.ui
@pytest.mark.smoke
class TestLogin:
    """Login test suite"""

    def test_successful_login_with_valid_credentials(self, page: Page):
        """
        Test successful login with valid credentials

        Steps:
        1. Navigate to login page
        2. Enter valid username and password
        3. Click login button
        4. Verify user is on dashboard
        """
        logger.info(" TEST: Successful login with valid credentials")

        # Arrange
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)

        # Act
        login_page.navigate()
        login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)

        # Assert
        dashboard_page.assert_on_dashboard()
        assert dashboard_page.is_dashboard_loaded(), "Dashboard should be loaded"

        logger.info(" TEST PASSED")

    def test_login_with_invalid_credentials(self, page: Page):
        """
        Test login fails with invalid credentials

        Steps:
        1. Navigate to login page
        2. Enter invalid username and password
        3. Click login button
        4. Verify error message is displayed
        """
        logger.info(" TEST: Login with invalid credentials")

        # Arrange
        login_page = LoginPage(page)

        # Act
        login_page.navigate()
        login_page.login("InvalidUser", "InvalidPass123")

        # Assert
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_message = login_page.get_error_message()
        assert "Invalid credentials" in error_message, \
            f"Expected 'Invalid credentials' in error, got: {error_message}"

        logger.info(" TEST PASSED")

    def test_login_with_empty_username(self, page: Page):
        """Test login fails with empty username"""
        logger.info(" TEST: Login with empty username")

        login_page = LoginPage(page)

        login_page.navigate()
        login_page.enter_password(ADMIN_PASSWORD)
        login_page.click_login_button()

        # OrangeHRM shows error only on username field, not global error
        # Check that we're still on login page
        assert "login" in login_page.get_current_url(), "Should stay on login page"

        logger.info(" TEST PASSED")

    def test_login_with_empty_password(self, page: Page):
        """Test login fails with empty password"""
        logger.info(" TEST: Login with empty password")

        login_page = LoginPage(page)

        login_page.navigate()
        login_page.enter_username(ADMIN_USERNAME)
        login_page.click_login_button()

        # Check that we're still on login page
        assert "login" in login_page.get_current_url(), "Should stay on login page"

        logger.info(" TEST PASSED")
    def test_login_page_elements_visible(self, page: Page):
        """Test all login page elements are visible"""
        logger.info(" TEST: Login page elements visible")

        login_page = LoginPage(page)

        login_page.navigate()

        assert login_page.is_login_page_loaded(), "Login page should be loaded"
        assert login_page.is_logo_visible(), "Logo should be visible"
        login_page.assert_element_visible(login_page.username_input, "Username field should be visible")
        login_page.assert_element_visible(login_page.password_input, "Password field should be visible")
        login_page.assert_element_visible(login_page.login_button, "Login button should be visible")

        logger.info(" TEST PASSED")