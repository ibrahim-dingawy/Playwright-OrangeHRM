"""
Admin User Management Tests (CRUD Operations)
"""
import pytest
from playwright.sync_api import Page
from tests.ui.pages.dashboard_page import DashboardPage
from tests.ui.pages.admin_page import AdminPage
from utilities.logger import get_logger
from utilities.generate_data import UserDataGenerator

logger = get_logger(__name__)


@pytest.mark.ui
@pytest.mark.regression
class TestAdminCRUD:
    """Admin CRUD operations test suite"""

    def test_navigate_to_admin_page(self, authenticated_page: Page):
        """Test navigation to Admin page"""
        logger.info(" TEST: Navigate to Admin page")

        dashboard = DashboardPage(authenticated_page)
        admin_page = AdminPage(authenticated_page)

        dashboard.navigate_to_admin()

        admin_page.assert_on_admin_page()
        assert admin_page.is_admin_page_loaded(), "Admin page should be loaded"

        logger.info(" TEST PASSED")

    def test_search_existing_user(self, authenticated_page: Page):
        """Test searching for existing user"""
        logger.info(" TEST: Search existing user")

        dashboard = DashboardPage(authenticated_page)
        admin_page = AdminPage(authenticated_page)

        # Navigate to Admin
        dashboard.navigate_to_admin()

        # Search for Admin user
        admin_page.search_by_username("Admin")

        # Verify results
        row_count = admin_page.get_table_row_count()
        assert row_count > 0, f"Should find at least one user, but found: {row_count}"

        # Check if Admin user is in results
        is_found = admin_page.is_user_found_in_table("Admin")
        assert is_found, "Admin user should be found in search results"

        logger.info(" TEST PASSED")

    def test_search_non_existing_user(self, authenticated_page: Page):
        """Test searching for non-existing user"""
        logger.info(" TEST: Search non-existing user")

        dashboard = DashboardPage(authenticated_page)
        admin_page = AdminPage(authenticated_page)

        dashboard.navigate_to_admin()

        # Search for non-existing user
        admin_page.search_by_username("NonExistingUser12345")

        # Verify no results
        row_count = admin_page.get_table_row_count()
        assert row_count == 0, f"Should find no users, but found: {row_count}"

        # Check for "No Records" message - use .first to avoid strict mode
        no_records = authenticated_page.locator("text=No Records Found").first
        assert no_records.is_visible(timeout=5000), "No records message should be visible"

        logger.info(" TEST PASSED")
    def test_reset_search_filters(self, authenticated_page: Page):
        """Test reset button clears search filters"""
        logger.info(" TEST: Reset search filters")

        dashboard = DashboardPage(authenticated_page)
        admin_page = AdminPage(authenticated_page)

        dashboard.navigate_to_admin()

        # Search for a user
        admin_page.search_by_username("Admin")

        # Reset filters
        admin_page.click_reset()
        authenticated_page.wait_for_timeout(1000)

        # Verify filters cleared (more results should appear)
        assert admin_page.get_table_row_count() > 0, "Should show all users after reset"

        logger.info(" TEST PASSED")

    def test_open_add_user_form(self, authenticated_page: Page):
        """Test opening Add User form"""
        logger.info(" TEST: Open Add User form")

        dashboard = DashboardPage(authenticated_page)
        admin_page = AdminPage(authenticated_page)

        dashboard.navigate_to_admin()
        admin_page.click_add_button()

        # Verify form elements visible
        admin_page.assert_element_visible(admin_page.user_role_field, "User role field should be visible")
        admin_page.assert_element_visible(admin_page.employee_name_field, "Employee name field should be visible")
        admin_page.assert_element_visible(admin_page.username_field, "Username field should be visible")
        admin_page.assert_element_visible(admin_page.save_button, "Save button should be visible")

        logger.info(" TEST PASSED")

    @pytest.mark.skip(reason="Requires valid employee name - may fail due to data constraints")
    def test_add_new_user(self, authenticated_page: Page):
        """
        Test adding a new user (SKIPPED - requires valid employee)

        Note: This test is skipped because it requires a valid employee name
        which may not exist in the demo environment.
        """
        logger.info(" TEST: Add new user (SKIPPED)")

        dashboard = DashboardPage(authenticated_page)
        admin_page = AdminPage(authenticated_page)

        # Generate test data
        user_data = UserDataGenerator.generate_user()

        dashboard.navigate_to_admin()
        admin_page.click_add_button()

        # Fill form
        admin_page.fill_add_user_form(
            user_role="Admin",
            employee_name="Test Employee",
            status="Enabled",
            username=user_data['username'],
            password="Test@123456"
        )

        admin_page.click_save()

        # Verify success
        admin_page.assert_user_added_successfully()

        logger.info(" TEST PASSED")