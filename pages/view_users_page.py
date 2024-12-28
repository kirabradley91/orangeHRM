from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ViewUsersPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # URL and page title
    URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
    PAGE_TITLE = 'OrangeHRM'
    PAGE_URL = 'viewSystemUsers'

    # Element Locators
    ADD_BUTTON = (By.XPATH, "//button[text()=' Add ']")
    USERNAME_LABEL = (By.XPATH, "//*[text()='Username']")
    USER_SEARCH_BUTTON = (By.XPATH, "//button[text()=' Search ']")
    DELETE_ICON = (By.CSS_SELECTOR, "i.bi-trash")
    DELETE_MESSAGE = (By.XPATH, "//div[contains(text(), 'Successfully Deleted')]")

    # Methods
    def load_and_validate_page(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains(self.PAGE_URL))
        self.wait.until(EC.title_contains(self.PAGE_TITLE))

    def validate_page(self):
        self.wait.until(EC.url_contains(self.PAGE_URL))
        self.wait.until(EC.title_contains(self.PAGE_TITLE))

    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def user_search(self, username):
        user_name_element = self.wait.until(EC.element_to_be_clickable(self.USERNAME_LABEL))
        element_below_user_name_element = self.driver.find_element(locate_with(By.TAG_NAME, "input").below(user_name_element))
        element_below_user_name_element.click()
        element_below_user_name_element.send_keys(username)
        user_search_button = self.wait.until(EC.element_to_be_clickable(self.USER_SEARCH_BUTTON))
        user_search_button.click()

    def delete_and_validate_user(self):
        # Click on delete icon
        delete_icon = self.wait.until(EC.element_to_be_clickable(self.DELETE_ICON))
        delete_icon.click()

        # Validate that the delete message is displayed on the UI
        delete_message = self.wait.until(EC.visibility_of_element_located(self.DELETE_MESSAGE))
        assert delete_message.is_displayed()