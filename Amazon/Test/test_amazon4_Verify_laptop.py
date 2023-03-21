import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Amazon.Pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class Test4:
    def test_laptop(self):
        homepage = HomePage(self.driver)
        homepage.search_element("laptop")
        homepage.search_submit()
        time.sleep(2)
        assert "laptop" in self.driver.title
