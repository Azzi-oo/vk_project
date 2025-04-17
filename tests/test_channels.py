import pytest
from tests.base import BaseTest
from config import TEST_CHANNEL

class TestChannels(BaseTest):
    def setup_method(self):
        super().setup_method()
        # Login before each test
        self.login()
        # Create a team for channel tests
        team_response = self.create_team(TEST_TEAM)
        assert team_response.status_code == 201
        self.team_id = team_response.json()['id']

    def test_create_channel(self):
        """Test successful channel creation"""
        response = self.create_channel(self.team_id, TEST_CHANNEL)
        assert response.status_code == 201
        channel_data = response.json()
        assert channel_data['name'] == TEST_CHANNEL['name']
        assert channel_data['display_name'] == TEST_CHANNEL['display_name']
        assert channel_data['type'] == TEST_CHANNEL['type']

    def test_create_duplicate_channel(self):
        """Test creating a channel with an existing name"""
        # First create a channel
        self.create_channel(self.team_id, TEST_CHANNEL)
        
        # Try to create another channel with the same name
        response = self.create_channel(self.team_id, TEST_CHANNEL)
        assert response.status_code == 400

    def test_send_message(self):
        """Test sending a message to a channel"""
        # First create a channel
        channel_response = self.create_channel(self.team_id, TEST_CHANNEL)
        channel_id = channel_response.json()['id']
        
        # Send a message
        message = "Test message"
        response = self.send_message(channel_id, message)
        assert response.status_code == 201
        message_data = response.json()
        assert message_data['message'] == message
        assert message_data['channel_id'] == channel_id

    def test_get_channel_messages(self):
        """Test retrieving messages from a channel"""
        # Create a channel and send a message
        channel_response = self.create_channel(self.team_id, TEST_CHANNEL)
        channel_id = channel_response.json()['id']
        self.send_message(channel_id, "Test message")
        
        # Get messages
        response = self.session.get(
            f"{self.MATTERMOST_URL}{self.ENDPOINTS['posts']}/channel/{channel_id}",
            headers=self.headers
        )
        assert response.status_code == 200
        posts = response.json()
        assert len(posts['posts']) > 0 