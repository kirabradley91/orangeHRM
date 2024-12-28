import requests

def get_and_validate_user_records(username, role, employee_name, status, headers=None, api_url= 'https://opensource-demo.orangehrmlive.com/api/v1/', ):

    # Make a GET request to the API

    response = requests.get(f"{api_url}/users?username={username}", headers=headers)

    # Validate the response headers
    if response.headers.get('Content-Type') != 'application/json':
        print("Error: Response content is not JSON")
        return None

    # Validate the response status code is 200
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return None

    user_records = response.json()

    # Validate the response body
    user_found = False
    for user in user_records:
        if (user['username'] == username and
            user['role'] == role and
            user['employee_name'] == employee_name and
            user['status'] == status):
            user_found = True
            break

    assert user_found, f"Error: User with username {username}, role {role}, employee name {employee_name}, and status {status} not found in the response"