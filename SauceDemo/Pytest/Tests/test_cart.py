import time
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import NoSuchElementException
from Pytest.Common.common import Common
from Pytest.Pages.Login import LoginPage
from Pytest.Pages.add_to_cart import AddCart
from Pytest.Tests.conftest import browser
import pyautogui

def test_cart(browser):
    home = Common(browser)
    addproduct = AddCart(browser)

    home.load_page()
    home.common_login("standard_user", "secret_sauce")
    pyautogui.press('enter')
    time.sleep(1)

    addproduct.product_list()
    addproduct.select_product_by_index(0)
    home.add_cart_button()
    time.sleep(1)

    home.cart_button()
    time.sleep(1)

    cart_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.is_displayed(), "Cart badge is not visible after adding a product."


def test_verify_product(browser):
    load = Common(browser)
    addproducts = AddCart(browser)
    load.load_page()
    load.common_login("standard_user","secret_sauce")
    pyautogui.press('enter')
    time.sleep(1)

    # Step 2: Get product list and extract name by index
    index = 0
    products = addproducts.product_list()
    selected_product_name = products[index].text

    # Step 3: Click product and add to cart
    addproducts.select_product_by_index(index)
    load.add_cart_button()
    time.sleep(1)

    # Step 4: Go to cart page
    load.cart_badge_button()
    time.sleep(1)

    # Step 5: Get product name from cart
    cart_product_element = browser.find_element(By.CLASS_NAME, "inventory_item_name")
    cart_product_name = cart_product_element.text

    #  Step 6: Assertion
    assert selected_product_name == cart_product_name, \
        f"Mismatch: Expected '{selected_product_name}', but got '{cart_product_name}' in cart"


def test_remove_cart(browser):
    load = Common(browser)
    add = AddCart(browser)
    load.load_page()
    load.common_login("standard_user","secret_sauce")
    pyautogui.press('enter')
    time.sleep(1)

    add.product_list()
    add.select_product_by_index(0)  # Select any index
    load.add_cart_button()
    time.sleep(1)

    load.cart_badge_button()
    time.sleep(1)
    load.remove_cart()
    time.sleep(1)
    try:
        browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert False, "Cart badge is still visible after removing item."
    except NoSuchElementException:
        assert True  # Passes as badge is not found