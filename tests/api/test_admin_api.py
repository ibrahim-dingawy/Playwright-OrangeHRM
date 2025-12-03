"""
API Admin Tests
"""
import pytest
from utilities.api_client import APIClient
from config.settings import BASE_URL
from utilities.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.api
@pytest.mark.skip(reason="Full API testing requires authentication setup")
class TestAdminAPI:
    """Admin API tests"""

    @pytest.fixture
    def api_client(self):
        """Create API client"""
        return APIClient(base_url=BASE_URL)

    def test_api_endpoint_exists(self, api_client):
        """Test that admin API endpoint exists"""
        logger.info("🧪 API TEST: Admin endpoint exists")

        response = api_client.get("/web/index.php/api/v2/admin/users")

        # Should return 401 (not 404), meaning endpoint exists
        assert response.status_code != 404, "Admin API endpoint should exist"

        logger.info("✅ TEST PASSED")