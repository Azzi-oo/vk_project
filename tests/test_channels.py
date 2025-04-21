import pytest
from .base import BaseTest
from config import TEST_CHANNEL, TEST_TEAM, MATTERMOST_URL, ENDPOINTS

class TestChannels(BaseTest):
    def setup_method(self):
        super().setup_method()
        response = self.login()
        if response.status_code == 401:
            pytest.skip("Invalid credentials. Please check your .env file")
        
        team_response = self.create_team(TEST_TEAM)
        if team_response.status_code == 401:
            pytest.skip("Not authorized to create teams. Please check user permissions")
        assert team_response.status_code == 201
        self.team_id = team_response.json()['id']

    def test_create_channel(self):
        """проверка канала о создании"""
        response = self.create_channel(self.team_id, TEST_CHANNEL)
        assert response.status_code == 201
        channel_data = response.json()
        assert channel_data['name'] == TEST_CHANNEL['name']
        assert channel_data['display_name'] == TEST_CHANNEL['display_name']
        assert channel_data['type'] == TEST_CHANNEL['type']

    def test_create_duplicate_channel(self):
        """попытка создать канал с занятым названием."""
        self.create_channel(self.team_id, TEST_CHANNEL)
        
        response = self.create_channel(self.team_id, TEST_CHANNEL)
        assert response.status_code == 400

    def test_send_message(self):
        """отправка сообщения в канал"""
        channel_response = self.create_channel(self.team_id, TEST_CHANNEL)
        channel_id = channel_response.json()['id']
        
        message = "Test message"
        response = self.send_message(channel_id, message)
        assert response.status_code == 201
        message_data = response.json()
        assert message_data['message'] == message
        assert message_data['channel_id'] == channel_id

    def test_get_channel_messages(self):
        """извлечение сообщений из канала"""
        channel_response = self.create_channel(self.team_id, TEST_CHANNEL)
        channel_id = channel_response.json()['id']
        self.send_message(channel_id, "Test message")
        
        response = self.session.get(
            f"{MATTERMOST_URL}{ENDPOINTS['posts']}/channel/{channel_id}",
            headers=self.headers
        )
        assert response.status_code == 200
        posts = response.json()
        assert len(posts['posts']) > 0 