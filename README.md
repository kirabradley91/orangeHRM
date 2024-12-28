# My Project

This project is a Selenium-based UI testing framework with backend validation using MySQL and API validation using Requests for REST API.
The framework is using Selenium WebDriver, Python, PyTest, Allure, WebDriverManager, Requests and MySQL Connector.
## Description

The project includes:
- UI tests using Selenium WebDriver.
- db_utils.py for Backend validation using MySQL.
- api_utils.py for API validation for REST API using requests.
- conftest.py for fixtures and configuration. Currently supporting only Chrome browser.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running UI Tests

1. Update the `db_config` fixture in `conftest.py` with your database configuration.
2. Update the `api_url` and `headers` in `api_utils.py` with your API endpoint and headers.
2. Run the tests using pytest:
    pytest tests/test_user_flow.py
    ```

## Tests Flow Description

### Test: `test_user_add`

This test adds users via the UI and validates their creation in the backend database.

### Test: `test_user_search`

This test searches for users via the UI and validates their information using the API.

### Test: `test_user_deleted`

This test deletes a user via the UI and validates their deletion on UI and in the backend database.
 