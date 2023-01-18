import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
FULL_NAME = '//input[@id="userName"]'
EMAIL = '//input[@id="userEmail"]'
CURRENT_ADDRESS = '//textarea[@id="currentAddress"]'
PERMANENT_ADDRESS = '//textarea[@id="permanentAddress"]'
SUBMIT = '//button[@id="submit"]'


@pytest.mark.usefixtures('setup')
class TestPageTextBox:

    def test_output_data_on_fields(self, setup):
        driver = setup
        full_name = driver.find_element(By.XPATH, FULL_NAME)
        email = driver.find_element(By.XPATH, EMAIL)
        current_address = driver.find_element(By.XPATH, CURRENT_ADDRESS)
        permanent_address = driver.find_element(By.XPATH, PERMANENT_ADDRESS)
        submit = driver.find_element(By.XPATH, SUBMIT)

        full_name.send_keys('Sergey')
        email.send_keys('abc@email.com')
        current_address.send_keys('asdfasdfas')
        permanent_address.send_keys('dfasdfasdfsa')
        submit.click()


