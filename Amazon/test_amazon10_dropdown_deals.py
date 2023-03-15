import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Test10:
    def test_deals(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "searchDropdownBox").send_keys('Books')
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        assert (self.driver.page_source.find("Books"))


