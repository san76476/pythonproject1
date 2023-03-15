import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Test9:
    def test_cart(self):
        time.sleep(2)
        self.drive.find_element(By.ID, "nav-cart-count-container").click()
        assert (self.driver.page_source.find("Cart is empty"))


