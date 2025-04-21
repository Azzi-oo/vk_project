import os
from dotenv import load_dotenv

load_dotenv()

MATTERMOST_URL = os.getenv('MATTERMOST_URL', 'http://localhost:8065')
API_VERSION = 'v4'

TEST_USER = {
    'username': os.getenv('TEST_USERNAME', 'testuser'),
    'password': os.getenv('TEST_PASSWORD', 'testpassword'),
    'email': os.getenv('TEST_EMAIL', 'test@example.com')
}

ENDPOINTS = {
    'login': f'/api/{API_VERSION}/users/login',
    'users': f'/api/{API_VERSION}/users',
    'channels': f'/api/{API_VERSION}/channels',
    'teams': f'/api/{API_VERSION}/teams',
    'posts': f'/api/{API_VERSION}/posts'
}

TEST_CHANNEL = {
    'name': 'test-channel',
    'display_name': 'Test Channel',
    'type': 'O'
}

TEST_TEAM = {
    'name': 'test-team',
    'display_name': 'Test Team',
    'type': 'O' 
} 