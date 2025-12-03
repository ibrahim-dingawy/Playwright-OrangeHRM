"""
API Login Tests
"""
import pytest
import requests
from utilities.api_client import APIClient
from config.settings import BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from utilities.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.api
class TestLoginAPI:
    """Login API test suite"""

    @pytest.fixture
    def api_client(self):
        """Create API client"""
        return APIClient(base_url=BASE_URL)

    def test_api_health_check(self, api_client):
        """Test API health check endpoint"""
        logger.info(" API TEST: Health check")

        try:
            response = api_client.get("/web/index.php/api/v2/dashboard/employees/time-at-work")

            # Just verify we can reach the API
            assert response.status_code in [200, 401, 403], \
                f"Expected valid status code, got: {response.status_code}"

            logger.info(" API is reachable")

        except requests.exceptions.RequestException as e:
            logger.warning(f"API health check failed: {e}")
            pytest.skip("API endpoint not accessible")

    def test_api_without_authentication(self, api_client):
        """Test API calls without authentication return 401"""
        logger.info(" API TEST: Unauthorized access")

        response = api_client.get("/web/index.php/api/v2/admin/users")

        assert response.status_code == 401, \
            f"Expected 401 Unauthorized, got: {response.status_code}"

        logger.info(" TEST PASSED")

    @pytest.mark.skip(reason="Authentication flow needs to be implemented")
    def test_get_users_with_valid_token(self, api_client):
        """
        Test getting users list with valid authentication

        Note: Skipped because OrangeHRM demo may not support direct API auth
        """
        logger.info(" API TEST: Get users with auth (SKIPPED)")

        # This would require proper authentication flow
        # which may not be available in demo environment

        logger.info(" TEST SKIPPED")