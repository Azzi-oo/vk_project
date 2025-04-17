import requests
import pytest
from config import MATTERMOST_URL, ENDPOINTS, TEST_USER

class BaseTest:
    def setup_method(self):
        self.session = requests.Session()
        self.token = None
        self.headers = {
            'Content-Type': 'application/json'
        }

    def teardown_method(self):
        if self.token:
            self.logout()

    def login(self, username=None, password=None):
        """Login to Mattermost and store the token"""
        login_data = {
            'login_id': username or TEST_USER['username'],
            'password': password or TEST_USER['password']
        }
        response = self.session.post(
            f"{MATTERMOST_URL}{ENDPOINTS['login']}",
            json=login_data
        )
        if response.status_code == 200:
            self.token = response.headers.get('Token')
            self.headers['Authorization'] = f'Bearer {self.token}'
        return response

    def logout(self):
        """Logout from Mattermost"""
        if self.token:
            self.session.post(
                f"{MATTERMOST_URL}{ENDPOINTS['login']}/logout",
                headers=self.headers
            )
            self.token = None
            self.headers.pop('Authorization', None)

    def create_channel(self, team_id, channel_data):
        """Create a new channel"""
        return self.session.post(
            f"{MATTERMOST_URL}{ENDPOINTS['channels']}",
            headers=self.headers,
            json=channel_data
        )

    def create_team(self, team_data):
        """Create a new team"""
        return self.session.post(
            f"{MATTERMOST_URL}{ENDPOINTS['teams']}",
            headers=self.headers,
            json=team_data
        )

    def send_message(self, channel_id, message):
        """Send a message to a channel"""
        return self.session.post(
            f"{MATTERMOST_URL}{ENDPOINTS['posts']}",
            headers=self.headers,
            json={
                'channel_id': channel_id,
                'message': message
            }
        ) 