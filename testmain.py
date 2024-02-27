import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains



@pytest.mark.register
def test_register(setUp):
    driver = setUp
    print("test")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@placeholder='First Name']"))
    )
    Fname = driver.find_element(By.XPATH, "//*[@placeholder='First Name']")
    Lname = driver.find_element(By.XPATH, "//*[@placeholder='Last Name']")
    action = ActionChains(driver)
    action.click(Fname).send_keys("Muhammad").perform()
    action.click(Lname).send_keys("Asad").perform()
    checkbox = driver.find_element(By.ID, "checkbox1")
    action.click(checkbox).perform()
    time.sleep(3)

