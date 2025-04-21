import pytest
from .base import BaseTest
from config import TEST_USER, MATTERMOST_URL, ENDPOINTS

class TestAuthentication(BaseTest):
    def test_successful_login(self):
        """Test successful login with correct credentials"""
        response = self.login()
        # Mattermost returns 401 for invalid credentials
        if response.status_code == 401:
            pytest.skip("Invalid credentials. Please check your .env file")
        assert response.status_code == 200
        assert self.token is not None
        assert 'Authorization' in self.headers

    def test_invalid_credentials(self):
        """Test login with incorrect credentials"""
        response = self.login(username='wronguser', password='wrongpass')
        assert response.status_code == 401
        assert self.token is None
        assert 'Authorization' not in self.headers

    def test_empty_credentials(self):
        """Test login with empty credentials"""
        response = self.login(username='', password='')
        # Mattermost returns 401 for empty credentials
        assert response.status_code == 401
        assert self.token is None
        assert 'Authorization' not in self.headers

    def test_missing_credentials(self):
        """Test login with missing credentials"""
        response = self.session.post(
            f"{MATTERMOST_URL}{ENDPOINTS['login']}",
            json={}
        )
        # Mattermost returns 400 for missing credentials
        assert response.status_code == 400
        assert self.token is None
        assert 'Authorization' not in self.headers

    def test_logout(self):
        """Test successful logout"""
        # First login
        response = self.login()
        if response.status_code == 401:
            pytest.skip("Invalid credentials. Please check your .env file")
        assert self.token is not None
        
        # Then logout
        self.logout()
        assert self.token is None
        assert 'Authorization' not in self.headers 