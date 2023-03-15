import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Test5:
    def test_iPhone_neg(self):
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
        time.sleep(2)  #
        assert (self.driver.page_source.find("xyzqwe"))
