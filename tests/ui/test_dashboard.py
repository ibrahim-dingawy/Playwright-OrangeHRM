"""
Dashboard Tests
"""
import pytest
from playwright.sync_api import Page
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.dashboard_page import DashboardPage
from utilities.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.ui
@pytest.mark.smoke
class TestDashboard:
    """Dashboard test suite"""

    def test_dashboard_loads_after_login(self, authenticated_page: Page):
        """Test dashboard loads successfully after login"""
        logger.info(" TEST: Dashboard loads after login")

        dashboard = DashboardPage(authenticated_page)

        assert dashboard.is_dashboard_loaded(), "Dashboard should be loaded"
        assert "Dashboard" in dashboard.get_dashboard_title(), "Dashboard title should be visible"
        dashboard.assert_on_dashboard()

        logger.info(" TEST PASSED")

    def test_navigate_to_admin_from_dashboard(self, authenticated_page: Page):
        """Test navigation to Admin page from dashboard"""
        logger.info(" TEST: Navigate to Admin from dashboard")

        dashboard = DashboardPage(authenticated_page)

        dashboard.navigate_to_admin()

        dashboard.assert_url_contains("/admin")
        dashboard.assert_element_visible(dashboard.admin_menu, "Admin menu should be highlighted")

        logger.info(" TEST PASSED")

    def test_navigate_to_pim_from_dashboard(self, authenticated_page: Page):
        """Test navigation to PIM page from dashboard"""
        logger.info(" TEST: Navigate to PIM from dashboard")

        dashboard = DashboardPage(authenticated_page)

        dashboard.navigate_to_pim()

        dashboard.assert_url_contains("/pim")

        logger.info(" TEST PASSED")

    def test_logout_from_dashboard(self, authenticated_page: Page):
        """Test logout functionality"""
        logger.info(" TEST: Logout from dashboard")

        dashboard = DashboardPage(authenticated_page)
        login_page = LoginPage(authenticated_page)

        dashboard.logout()

        login_page.assert_on_login_page()
        assert login_page.is_login_page_loaded(), "Should return to login page"

        logger.info(" TEST PASSED")

    def test_all_menu_items_visible(self, authenticated_page: Page):
        """Test all main menu items are visible"""
        logger.info(" TEST: All menu items visible")

        dashboard = DashboardPage(authenticated_page)

        dashboard.assert_element_visible(dashboard.admin_menu, "Admin menu should be visible")
        dashboard.assert_element_visible(dashboard.pim_menu, "PIM menu should be visible")
        dashboard.assert_element_visible(dashboard.leave_menu, "Leave menu should be visible")
        dashboard.assert_element_visible(dashboard.time_menu, "Time menu should be visible")
        dashboard.assert_element_visible(dashboard.recruitment_menu, "Recruitment menu should be visible")

        logger.info(" TEST PASSED")