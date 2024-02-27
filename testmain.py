import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options



@pytest.mark.parametrize("Username , Password", [("student","Password123"),("student1","Password123"),("student2","Password123")])
def test_register(setUp,Username,Password):
    driver = setUp

 
    input_username = driver.find_element(By.ID, "username")
    input_password = driver.find_element(By.ID, "password")
    submit = driver.find_element(By.ID, "submit")

    action = ActionChains(driver)
    action.click(input_username).send_keys(Username).perform()
    action.click(input_password).send_keys(Password).perform()
    action.click(submit).perform()
    
    time.sleep(8)

    title = driver.title
    expected = "Logged In Successfully | Practice Test Automation"
    print("Title of the page is " + title)
    assert title == expected, f"Expected title: {expected}, but got {title}"
    time.sleep(3)

