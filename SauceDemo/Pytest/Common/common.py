from selenium.webdriver.common.by import By
import time

class Common:
    def __init__(self, driver):
        self.driver = driver


    def load_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def common_login(self,username,password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(2)


    def add_cart_button(self):
        self.driver.find_element(By.ID ,"add-to-cart").click()
        time.sleep(1)

    def remove_cart(self):
        self.driver.find_element(By.ID,"remove-sauce-labs-backpack").click()
        time.sleep(1)

    def cart_badge_button(self):
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").click()

    def sort_item(self):
        self.driver.find_element(By.CLASS_NAME,"product_sort_container").click()
        time.sleep(1)

    def get_product_name(self):
        product_name = self.driver.find_element(By.CLASS_NAME, "inventory_item_name")
        return product_name.text

    def common_logout(self):
        self.driver.find_element(By.ID,"react-burger-menu-btn").click()
        self.driver.find_element(By.ID,"logout_sidebar_link").click()
