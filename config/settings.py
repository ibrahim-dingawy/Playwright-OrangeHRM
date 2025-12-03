"""
Configuration settings for the test framework
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project root directory
ROOT_DIR = Path(__file__).parent.parent

# URLs
BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/")
API_BASE_URL = os.getenv("API_BASE_URL", f"{BASE_URL}web/index.php/api/v2")

# Credentials
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

# Browser Settings
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
TIMEOUT = int(os.getenv("TIMEOUT", "30000"))

# Viewport
VIEWPORT_WIDTH = 1920
VIEWPORT_HEIGHT = 1080

# Screenshots & Videos
SCREENSHOT_ON_FAILURE = True
VIDEO_ON_FAILURE = True
TRACE_ON_FAILURE = True

# Reports
REPORTS_DIR = ROOT_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
VIDEOS_DIR = REPORTS_DIR / "videos"
TRACES_DIR = REPORTS_DIR / "traces"

# Create directories
for directory in [REPORTS_DIR, SCREENSHOTS_DIR, VIDEOS_DIR, TRACES_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# API Settings
API_TIMEOUT = 30
API_RETRY_COUNT = 3

# Test Data
TEST_DATA_DIR = ROOT_DIR / "config"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = REPORTS_DIR / "test_execution.log"


class TestUsers:
    """Test user credentials"""
    ADMIN = {
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
        "role": "Admin"
    }

    ESS_USER = {
        "username": "essuser",
        "password": "admin123",
        "role": "ESS"
    }


class URLs:
    """Application URLs"""
    BASE = BASE_URL
    LOGIN = f"{BASE_URL}web/index.php/auth/login"
    DASHBOARD = f"{BASE_URL}web/index.php/dashboard/index"
    ADMIN = f"{BASE_URL}web/index.php/admin/viewSystemUsers"
    PIM = f"{BASE_URL}web/index.php/pim/viewEmployeeList"
    LEAVE = f"{BASE_URL}web/index.php/leave/viewLeaveList"
    TIME = f"{BASE_URL}web/index.php/time/viewEmployeeTimesheet"
    RECRUITMENT = f"{BASE_URL}web/index.php/recruitment/viewCandidates"


class APIEndpoints:
    """API endpoints"""
    BASE = API_BASE_URL
    LOGIN = f"{API_BASE_URL}/auth/login"
    USERS = f"{API_BASE_URL}/admin/users"
    EMPLOYEES = f"{API_BASE_URL}/pim/employees"
    LEAVE = f"{API_BASE_URL}/leave/leave-requests"


# Print config on import (for debugging)
if __name__ == "__main__":
    print("Configuration loaded:")
    print(f"  Base URL: {BASE_URL}")
    print(f"  Browser: {BROWSER}")
    print(f"  Headless: {HEADLESS}")
    print(f"  Reports: {REPORTS_DIR}")