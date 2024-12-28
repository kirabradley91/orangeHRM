import pytest

from pages.add_user_page import AddUserPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.view_users_page import ViewUsersPage
from tests.api_utils import get_and_validate_user_records
from tests.db_utils import is_user_deleted, is_user_created


@pytest.mark.regressiontest
def test_user_add(browser):
    login_page = LoginPage(browser)
    view_users_page = ViewUsersPage(browser)
    add_user_page = AddUserPage(browser)
    dashboard_page = DashboardPage(browser)

    # navigate to login page and log in as Admin
    login_page.load_and_validate_page()
    login_page.admin_login()

    # validate the user is on the dashboard page and click on Admin menu link
    dashboard_page.validate_page()
    dashboard_page.click_admin_menu_link()

    # validate the user is on the view users page and click on Add button
    view_users_page.validate_page()
    view_users_page.click_add_button()

    # add user
    add_user_page.validate_page()
    add_user_page.add_user("testUser1", "Emily", "Emily Jones", "Password123", "Password123", "Admin", "Enabled")

    # click on Reset and validated that the fields are cleared
    add_user_page.click_reset_button()
    add_user_page.validate_reset()

    # add user and save
    add_user_page.add_user("testUser1", "Emily", "Emily Jones", "Password123", "Password123", "Admin", "Enabled")
    add_user_page.click_save_button()
    assert is_user_created(db_config, "testUser1")

    # add another user and save
    view_users_page.validate_page()
    view_users_page.click_add_button()
    add_user_page.add_user("testUser2", "Emily", "Emily Jones", "Password123", "Password123", "ESS", "Disabled")
    add_user_page.click_save_button()
    assert is_user_created(db_config, "testUser2")

@pytest.mark.regressiontest
def test_user_search(browser):
    login_page = LoginPage(browser)
    view_users_page = ViewUsersPage(browser)
    dashboard_page = DashboardPage(browser)

    # navigate to login page and log in as Admin
    login_page.load_and_validate_page()
    login_page.admin_login()

    # validate the user is on the dashboard page and click on Admin menu link
    dashboard_page.validate_page()
    dashboard_page.click_admin_menu_link()

    # validate the user is on the view users page and click on Add button
    view_users_page.validate_page()

    # search for a user
    view_users_page.user_search("testUser1")
    view_users_page.user_search("testUser2")

    # validate user from API response using api_utils.py

    testuser1_records = get_and_validate_user_records("testUser1", "Admin", "Emily Jones", "Enabled")
    testuser2_records = get_and_validate_user_records("testUser2", "ESS", "Emily Jones", "Disabled")


@pytest.mark.regressiontest
def test_user_deleted(browser, db_config):
    login_page = LoginPage(browser)
    view_users_page = ViewUsersPage(browser)
    dashboard_page = DashboardPage(browser)

    # navigate to login page and log in as Admin
    login_page.load_and_validate_page()
    login_page.admin_login()

    # validate the user is on the dashboard page and click on Admin menu link
    dashboard_page.validate_page()
    dashboard_page.click_admin_menu_link()

    # validate the user is on the view users page and click on Add button
    view_users_page.validate_page()

    # search for a user
    view_users_page.user_search("testUser2")

    # delete testUser2
    view_users_page.delete_and_validate_user("testUser2")

    # Validate that the user was deleted from the backend
    assert is_user_deleted(db_config, "testUser2")