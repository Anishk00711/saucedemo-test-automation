import time
from selenium.webdriver.common.by import By
from Pytest.Tests.conftest import browser


class AddCart:
    def __init__(self, driver):
        self.driver = driver


    def product_list(self):
        return self.driver.find_elements(By.CLASS_NAME,"inventory_item_name ")

    def select_product_by_index(self, index):
        products = self.product_list()

        if products and index < len(products):
            products[index].click()
        else:
            raise IndexError("Product index out of range or products not loaded")





