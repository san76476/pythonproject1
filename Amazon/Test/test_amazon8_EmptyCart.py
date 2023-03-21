import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Amazon.Pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class Test8:
    def test_cart(self):
        homepage = HomePage(self.driver)
        time.sleep(2)
        homepage.cart_click()
        assert (self.driver.page_source.find("Cart is empty"))


