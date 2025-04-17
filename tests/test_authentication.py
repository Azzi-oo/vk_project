import pytest
from tests.base import BaseTest
from config import TEST_USER

class TestAuthentication(BaseTest):
    def test_successful_login(self):
        """Test successful login with correct credentials"""
        response = self.login()
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
        assert response.status_code == 400
        assert self.token is None
        assert 'Authorization' not in self.headers

    def test_missing_credentials(self):
        """Test login with missing credentials"""
        response = self.session.post(
            f"{self.MATTERMOST_URL}{self.ENDPOINTS['login']}",
            json={}
        )
        assert response.status_code == 400
        assert self.token is None
        assert 'Authorization' not in self.headers

    def test_logout(self):
        """Test successful logout"""
        # First login
        self.login()
        assert self.token is not None
        
        # Then logout
        self.logout()
        assert self.token is None
        assert 'Authorization' not in self.headers 