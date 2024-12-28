from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # URL and page title
    URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    PAGE_TITLE = 'OrangeHRM'
    PAGE_URL = 'login'

    # Element Locators
    USERNAME = By.NAME, 'username'
    PASSWORD = By.NAME, 'password'
    LOGIN_BUTTON = By.XPATH, "//button[text()=' Login ']"

    # Methods
    def load_and_validate_page(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains(self.PAGE_URL))
        self.wait.until(EC.title_contains(self.PAGE_TITLE))

    def admin_login(self, username="Admin", password="admin123"):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
