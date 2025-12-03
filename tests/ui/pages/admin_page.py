"""
Admin Page Object
"""
from playwright.sync_api import Page
from tests.ui.pages.base_page import BasePage
from utilities.logger import get_logger

logger = get_logger(__name__)


class AdminPage(BasePage):
    """Admin Page interactions"""

    def __init__(self, page: Page):
        super().__init__(page)

        # Locators
        self.page_title = "h6:has-text('Admin')"
        self.add_button = "button:has-text('Add')"
        self.search_button = "button[type='submit']"
        self.reset_button = "button:has-text('Reset')"

        # Search fields
        self.username_search = "//label[text()='Username']/parent::div/following-sibling::div/input"
        self.user_role_dropdown = "//label[text()='User Role']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']"
        self.status_dropdown = "//label[text()='Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']"

        # Table
        self.table_row = ".oxd-table-card"
        self.delete_button = "button:has-text('Delete')"
        self.edit_button = "button:has-text('Edit')"

        # Add/Edit User Form
        self.user_role_field = "//label[text()='User Role']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']"
        self.employee_name_field = "input[placeholder='Type for hints...']"
        self.status_field = "//label[text()='Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']"
        self.username_field = "//label[text()='Username']/parent::div/following-sibling::div/input"
        self.password_field = "//label[text()='Password']/parent::div/following-sibling::div/input"
        self.confirm_password_field = "//label[text()='Confirm Password']/parent::div/following-sibling::div/input"
        self.save_button = "button[type='submit']"
        self.cancel_button = "button:has-text('Cancel')"

    def is_admin_page_loaded(self) -> bool:
        """Check if admin page is loaded"""
        return self.is_visible(self.page_title)

    def click_add_button(self):
        """Click Add button"""
        logger.info("Clicking Add button")
        self.click(self.add_button)
        self.wait_for_loading_to_disappear()

    def search_by_username(self, username: str):
        """
        Search user by username

        Args:
            username: Username to search
        """
        logger.info(f"Searching for username: {username}")
        self.fill(self.username_search, username)
        self.click(self.search_button)
        self.wait_for_loading_to_disappear()

    def click_reset(self):
        """Click Reset button"""
        logger.info("Clicking Reset button")
        self.click(self.reset_button)

    def get_table_row_count(self) -> int:
        """Get number of rows in table"""
        # Wait for table to load
        self.page.wait_for_timeout(1000)
        return self.page.locator(self.table_row).count()

    def is_user_found_in_table(self, username: str) -> bool:
        """Check if user exists in table"""
        try:
            # Wait for results
            self.page.wait_for_timeout(1000)

            # Search in table cells
            user_cell = self.page.locator(f".oxd-table-cell:has-text('{username}')")
            is_found = user_cell.count() > 0

            if is_found:
                logger.info(f"✅ User '{username}' found in table")
            else:
                logger.info(f"❌ User '{username}' not found in table")

            return is_found
        except Exception as e:
            logger.error(f"Error checking user in table: {e}")
            return False


    def click_first_delete_button(self):
        """Click delete button on first row"""
        logger.info("Clicking delete button on first row")
        self.page.locator(self.delete_button).first.click()

    def confirm_delete(self):
        """Confirm delete action"""
        logger.info("Confirming delete")
        self.click("button:has-text('Yes, Delete')")
        self.wait_for_loading_to_disappear()

    def fill_add_user_form(self, user_role: str, employee_name: str, status: str,
                           username: str, password: str):
        """
        Fill add user form

        Args:
            user_role: User role (Admin/ESS)
            employee_name: Employee name
            status: Status (Enabled/Disabled)
            username: Username
            password: Password
        """
        logger.info(f"Filling add user form for: {username}")

        # Select user role
        self.click(self.user_role_field)
        self.click(f"text={user_role}")

        # Enter employee name
        self.fill(self.employee_name_field, employee_name)
        self.page.wait_for_timeout(1000)  # Wait for autocomplete
        self.press_key(self.employee_name_field, "ArrowDown")
        self.press_key(self.employee_name_field, "Enter")

        # Select status
        self.click(self.status_field)
        self.click(f"text={status}")

        # Enter credentials
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.fill(self.confirm_password_field, password)

    def click_save(self):
        """Click Save button"""
        logger.info("Clicking Save button")
        self.click(self.save_button)
        self.wait_for_loading_to_disappear()

    # Assertions
    def assert_on_admin_page(self):
        """Assert user is on admin page"""
        self.assert_element_visible(self.page_title, "Admin page should be visible")
        self.assert_url_contains("/admin")
        logger.info("✅ On admin page")

    def assert_user_added_successfully(self):
        """Assert success message displayed"""
        self.assert_element_visible(".oxd-toast--success", "Success message should be displayed")
        logger.info("✅ User added successfully")