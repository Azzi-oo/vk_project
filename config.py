import os
from dotenv import load_dotenv

load_dotenv()

# Mattermost API Configuration
MATTERMOST_URL = os.getenv('MATTERMOST_URL', 'http://localhost:8065')
API_VERSION = 'v4'

# Test User Credentials
TEST_USER = {
    'username': os.getenv('TEST_USERNAME', 'testuser'),
    'password': os.getenv('TEST_PASSWORD', 'testpassword'),
    'email': os.getenv('TEST_EMAIL', 'test@example.com')
}

# API Endpoints
ENDPOINTS = {
    'login': f'/api/{API_VERSION}/users/login',
    'users': f'/api/{API_VERSION}/users',
    'channels': f'/api/{API_VERSION}/channels',
    'teams': f'/api/{API_VERSION}/teams',
    'posts': f'/api/{API_VERSION}/posts'
}

# Test Data
TEST_CHANNEL = {
    'name': 'test-channel',
    'display_name': 'Test Channel',
    'type': 'O'  # O for open channel, P for private
}

TEST_TEAM = {
    'name': 'test-team',
    'display_name': 'Test Team',
    'type': 'O'  # O for open team, I for invite-only
} 