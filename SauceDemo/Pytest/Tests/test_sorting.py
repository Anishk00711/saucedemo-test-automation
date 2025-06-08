import time
import pyautogui
from selenium.webdriver.common.by import By
from Pytest.Tests.conftest import browser

from Pytest.Common.common import Common


def test_sortingasc(browser):
    load = Common(browser)
    load.load_page()
    load.common_login("standard_user", "secret_sauce")
    pyautogui.press("enter")
    load.sort_item()
    pyautogui.press("enter")
    product_name_elements = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [name.text for name in product_name_elements]

    # Step 3: Verify the list is sorted alphabetically
    sorted_names = sorted(product_names)
    assert product_names == sorted_names, f"Products are not sorted A to Z: {product_names}"

def test_sortingdesc(browser):
    load = Common(browser)
    load.load_page()
    load.common_login("standard_user", "secret_sauce")
    pyautogui.press("enter")
    load.sort_item()
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(1)
    product_elements = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_names = [el.text for el in product_elements]

    # Check that product names are in descending order
    expected_order = sorted(product_names, reverse=True)
    assert product_names == expected_order, f"Products not sorted Z to A: {product_names}"

def test_sortingpricelow(browser):
    load = Common(browser)
    load.load_page()
    load.common_login("standard_user", "secret_sauce")
    pyautogui.press("enter")
    load.sort_item()
    pyautogui.press("down", presses=2)
    pyautogui.press("enter")
    time.sleep(1)
    price_elements = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(el.text.replace("$", "")) for el in price_elements]

    # Step 4: Verify prices are sorted in ascending order
    expected_order = sorted(prices)
    assert prices == expected_order, f"Prices not sorted low to high: {prices}"

def test_sortingpricehigh(browser):
    load = Common(browser)
    load.load_page()
    load.common_login("standard_user", "secret_sauce")
    pyautogui.press("enter")
    load.sort_item()
    pyautogui.press("down", presses=3)
    pyautogui.press("enter")
    time.sleep(1)
    # Step 3: Extract all product prices
    price_elements = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(el.text.replace("$", "")) for el in price_elements]

    # Step 4: Verify prices are sorted in descending order
    expected_order = sorted(prices, reverse=True)
    assert prices == expected_order, f"Prices not sorted high to low: {prices}"