from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # URL and page title
    URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser'
    PAGE_TITLE = 'OrangeHRM'
    PAGE_URL = 'saveSystemUser'

    # Element Locators
    EMPLOYEE_NAME = (By.XPATH, "//*[text()='Employee Name']")
    USER_ROLE = (By.XPATH, "//*[text()='User Role']")
    STATUS = (By.XPATH, "//*[text()='Status']")
    USERNAME = (By.XPATH, "//*[text()='Username']")
    PASSWORD = (By.XPATH, "//*[text()='Password']")
    CONFIRM_PASSWORD = (By.XPATH, "//*[text()='Confirm Password']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Reset']")

    # Methods

    def load_and_validate_page(self):
        self.driver.get(self.URL)
        assert self.PAGE_URL in self.driver.current_url
        assert self.PAGE_TITLE in self.driver.title

    def validate_page(self):
        self.wait.until(EC.url_contains(self.PAGE_URL))
        self.wait.until(EC.title_contains(self.PAGE_TITLE))

    def add_user(self, employee_name, username, full_username, password, confirm_password, user_role_option,
                 status_option):
        # Enter employee name
        employee_name_input = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "input").below(self.EMPLOYEE_NAME)))
        employee_name_input.click()
        employee_name_input.send_keys(employee_name)
        # Wait for auto-complete suggestions and select a value
        auto_complete_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{full_username}']")))
        auto_complete_option.click()

        # Select user role
        user_role_dropdown = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "div").below(self.USER_ROLE)))
        user_role_dropdown.click()
        user_role_option_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{user_role_option}']")))
        user_role_option_element.click()

        # Select status
        status_dropdown = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "div").below(self.STATUS)))
        status_dropdown.click()
        status_option_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{status_option}']")))
        status_option_element.click()

        # Enter username
        username_input = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "input").below(self.USERNAME)))
        username_input.click()
        username_input.send_keys(username)

        # Enter password
        password_input = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "input").below(self.PASSWORD)))
        password_input.click()
        password_input.send_keys(password)

        # Enter confirm password
        confirm_password_input = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "input").below(self.CONFIRM_PASSWORD)))
        confirm_password_input.click()
        confirm_password_input.send_keys(confirm_password)

    def click_reset_button(self):
        reset_button = self.wait.until(EC.element_to_be_clickable(self.RESET_BUTTON))
        reset_button.click()

    def validate_reset(self):
        # Check that all input fields are empty
        employee_name_input = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "input").below(self.EMPLOYEE_NAME)))
        assert employee_name_input.get_attribute("value") == ""

        username_input = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "input").below(self.USERNAME)))
        assert username_input.get_attribute("value") == ""

        password_input = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "input").below(self.PASSWORD)))
        assert password_input.get_attribute("value") == ""

        confirm_password_input = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "input").below(self.CONFIRM_PASSWORD)))
        assert confirm_password_input.get_attribute("value") == ""

        # Check that dropdowns are set to default values
        user_role_dropdown = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "div").below(self.USER_ROLE)))
        assert user_role_dropdown.text == "Select"

        status_dropdown = self.wait.until(
            EC.element_to_be_clickable(locate_with(By.TAG_NAME, "div").below(self.STATUS)))
        assert status_dropdown.text == "Enabled"

        # Check that the "Successfully Saved" message is not displayed
        assert not self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Successfully Saved')]")

    def click_save_button(self):
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']")))
        save_button.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Successfully Saved')]")))
