import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Test7:
    def test_logo(self):
        time.sleep(2)
        assert "Amazon.com. Spend less. Smile more." in self.driver.title

