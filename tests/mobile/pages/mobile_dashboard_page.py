from playwright.sync_api import Page

class MobileDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")
        self.quick_launch_widget = page.get_by_text("Quick Launch")