import time

import pyautogui
import pytest
from selenium.webdriver.common.by import By
from Pytest.Common.common import Common
from Pytest.Pages.Login import LoginPage
from Pytest.Tests.conftest import browser


@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce",),
    ("standard_user" ,"",),
    ("","secret_sauce")])



def test_login(browser, username, password):
    login = LoginPage(browser)
    login.load()
    login.login(username, password)
    if username == "standard_user" and password == "secret_sauce":
        assert login.login_success() is True
    elif username == "standard_user" and password == "":
        assert "Epic sadface: Password is required" in login.error_msg()
        print(login.error_msg())
    else:
        assert "Epic sadface: Username is required" in login.error_msg()
        print(login.error_msg())

    time.sleep(2)

def test_logout(browser):
    logout = Common(browser)
    logout.load_page()
    logout.common_login("standard_user","secret_sauce")
    pyautogui.press("enter")
    logout.common_logout()
    assert "saucedemo.com" in browser.current_url
    assert browser.find_element(By.ID, "login-button").is_displayed()