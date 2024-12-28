import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def browser():
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # make a screenshot before closing the browser
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    # when test is done, close ALL windows of the browser
    browser.quit()


@pytest.fixture()
def db_config():
    return {
        'host': 'your_db_host',
        'user': 'your_db_user',
        'password': 'your_db_password',
        'database': 'your_db_name'
    }