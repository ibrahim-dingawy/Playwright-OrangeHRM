
from playwright.sync_api import Page

class MobileLoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[role='alert']")

    def navigate(self):
        """Go to login page"""
        self.page.goto("/web/index.php/auth/login")

    def login(self, username: str, password: str):
        """
        Perform login action
        :param username: Admin username
        :param password: Admin password
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        # Wait for navigation to complete
        self.page.wait_for_load_state("networkidle")