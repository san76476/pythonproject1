from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    print("initiating chrome driver")
    s = Service("/chrome/chromedriver_win32/chromedriver.exe") #if not added in PATH
    driver = webdriver.Chrome(service=s)
    driver.get("http://amazon.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()