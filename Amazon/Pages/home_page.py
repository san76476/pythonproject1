import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_text_box = "twotabsearchtextbox"
        self.submit_button = "nav-search-submit-button"
        self.click_cart = "nav-cart-count-container"
        self.drop_down = "searchDropdownBox"

    def search_element(self, element):
        self.driver.find_element(By.ID, self.search_text_box).send_keys(element)

    def search_submit(self):
        self.driver.find_element(By.ID, self.submit_button).click()

    def cart_click(self):
        self.driver.find_element(By.ID, self.click_cart).click()

    def drop_down_select(self,element):
        self.driver.find_element(By.ID, self.drop_down).send_keys(element)