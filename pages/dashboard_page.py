from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # URL and page title
    URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    PAGE_TITLE = 'OrangeHRM'
    PAGE_URL = 'dashboard'

    # Element Locators
    ADMIN_MENU_LINK = (By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']")

    def validate_page(self):
        self.wait.until(EC.url_contains(self.PAGE_URL))
        self.wait.until(EC.title_contains(self.PAGE_TITLE))

    def click_admin_menu_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ADMIN_MENU_LINK)).click()
