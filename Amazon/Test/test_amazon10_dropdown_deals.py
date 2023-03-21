import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Amazon.Pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class Test10:
    def test_deals(self):
        homepage = HomePage(self.driver)
        time.sleep(1)
        homepage.drop_down_select("Deals")
        homepage.search_submit()
        assert (self.driver.page_source.find("Deals"))


