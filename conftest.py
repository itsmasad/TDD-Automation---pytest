import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


@pytest.fixture(scope="session", autouse=True)
def setUp():
    driver = webdriver.Chrome()
    website = "https://demo.automationtesting.in/Register.html"
    driver.get(website)
    yield driver
    driver.close()