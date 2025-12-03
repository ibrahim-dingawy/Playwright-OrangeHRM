"""
API User Management Tests
"""
import pytest
from utilities.api_client import APIClient
from config.settings import BASE_URL
from utilities.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.api
@pytest.mark.skip(reason="API authentication not fully supported in demo")
class TestUsersAPI:
    """User management API tests"""

    @pytest.fixture
    def api_client(self):
        """Create API client"""
        return APIClient(base_url=BASE_URL)

    def test_get_all_users(self, api_client):
        """Test getting all users"""
        logger.info(" API TEST: Get all users")

        response = api_client.get("/web/index.php/api/v2/admin/users")

        # Without auth, should return 401
        assert response.status_code == 401

        logger.info(" TEST PASSED")

    def test_get_user_by_id(self, api_client):
        """Test getting user by ID"""
        logger.info(" API TEST: Get user by ID")

        user_id = 1
        response = api_client.get(f"/web/index.php/api/v2/admin/users/{user_id}")

        # Without auth, should return 401
        assert response.status_code == 401

        logger.info(" TEST PASSED")