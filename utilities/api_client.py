"""
API client for OrangeHRM API testing
"""
import requests
from typing import Dict, Any, Optional
from utilities.logger import get_logger
from config.settings import API_BASE_URL, API_TIMEOUT

logger = get_logger(__name__)


class APIClient:
    """Base API client"""

    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _log_request(self, method: str, url: str, **kwargs):
        """Log request details"""
        logger.info(f"API Request: {method} {url}")
        if 'json' in kwargs:
            logger.debug(f"Request Body: {kwargs['json']}")

    def _log_response(self, response: requests.Response):
        """Log response details"""
        logger.info(f"API Response: {response.status_code}")
        try:
            logger.debug(f"Response Body: {response.json()}")
        except:
            logger.debug(f"Response Body: {response.text}")

    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """GET request"""
        url = f"{self.base_url}{endpoint}"
        self._log_request("GET", url, params=params)

        response = self.session.get(url, params=params, timeout=API_TIMEOUT, **kwargs)
        self._log_response(response)
        return response

    def post(self, endpoint: str, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """POST request"""
        url = f"{self.base_url}{endpoint}"
        self._log_request("POST", url, json=json)

        response = self.session.post(url, json=json, timeout=API_TIMEOUT, **kwargs)
        self._log_response(response)
        return response

    def put(self, endpoint: str, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """PUT request"""
        url = f"{self.base_url}{endpoint}"
        self._log_request("PUT", url, json=json)

        response = self.session.put(url, json=json, timeout=API_TIMEOUT, **kwargs)
        self._log_response(response)
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """DELETE request"""
        url = f"{self.base_url}{endpoint}"
        self._log_request("DELETE", url)

        response = self.session.delete(url, timeout=API_TIMEOUT, **kwargs)
        self._log_response(response)
        return response

    def set_auth_token(self, token: str):
        """Set authorization token"""
        self.session.headers.update({"Authorization": f"Bearer {token}"})
        logger.info("Authorization token set")


# Test the client
if __name__ == "__main__":
    client = APIClient()
    response = client.get("/health")
    print(f"Status: {response.status_code}")