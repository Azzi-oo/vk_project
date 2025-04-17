# Mattermost API Test Suite

This project contains automated tests for the Mattermost API, covering authentication, channel management, and message handling.

## Prerequisites

- Python 3.8 or higher
- Mattermost server running (local or remote)
- Access to Mattermost API

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root with the following variables:
   ```
   MATTERMOST_URL=http://your-mattermost-server:8065
   TEST_USERNAME=your-test-username
   TEST_PASSWORD=your-test-password
   TEST_EMAIL=your-test-email@example.com
   ```

## Running Tests

To run all tests:
```bash
pytest
```

To run specific test files:
```bash
pytest tests/test_authentication.py
pytest tests/test_channels.py
```

To generate an HTML report:
```bash
pytest --html=report.html
```

## Test Coverage

The test suite covers the following scenarios:

### Authentication
- Successful login with correct credentials
- Failed login with incorrect credentials
- Login with empty credentials
- Login with missing credentials
- Successful logout

### Channel Management
- Creating a new channel
- Creating a duplicate channel
- Sending messages to a channel
- Retrieving messages from a channel

## Test Structure

- `config.py`: Configuration settings and test data
- `tests/base.py`: Base test class with common functionality
- `tests/test_authentication.py`: Authentication test cases
- `tests/test_channels.py`: Channel management test cases

## Troubleshooting

If you encounter any issues:
1. Verify your Mattermost server is running and accessible
2. Check your `.env` file configuration
3. Ensure you have the correct permissions on the Mattermost server
4. Check the test logs for detailed error messages 