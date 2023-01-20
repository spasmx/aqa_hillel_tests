import pytest
import time
from selenium.webdriver.common.by import By

FULL_NAME_XPATH = '//input[@id="userName"]'
EMAIL_XPATH = '//input[@id="userEmail"]'
CURRENT_ADDRESS_XPATH = '//textarea[@id="currentAddress"]'
PERMANENT_ADDRESS_XPATH = '//textarea[@id="permanentAddress"]'
SUBMIT_XPATH = '//button[@id="submit"]'
OUTPUT_BOARD_ID = 'div[id="output"]'


@pytest.mark.usefixtures('setup')
class TestPageTextBox:

    def test_output_data_on_fields_xpath(self, setup):

        full_name = setup.find_element(By.XPATH, FULL_NAME_XPATH)
        email = setup.find_element(By.XPATH, EMAIL_XPATH)
        current_address = setup.find_element(By.XPATH, CURRENT_ADDRESS_XPATH)
        permanent_address = setup.find_element(By.XPATH, PERMANENT_ADDRESS_XPATH)
        submit = setup.find_element(By.XPATH, SUBMIT_XPATH)
        output_board = setup.find_element(By.CSS_SELECTOR, OUTPUT_BOARD_ID)

        full_name.send_keys('Sergey')
        email.send_keys('test@email.com')
        current_address.send_keys('test current address')
        permanent_address.send_keys('test permanent address')

        val_name = full_name.get_attribute('value')
        val_email = email.get_attribute('value')
        val_current_address = current_address.get_attribute('value')
        val_permanent_address = permanent_address.get_attribute('value')

        setup.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()
        setup.execute_script("arguments[0].scrollIntoView();", output_board)

        result_name = setup.find_element(By.CSS_SELECTOR, 'p[id="name"]').text
        result_email = setup.find_element(By.CSS_SELECTOR, 'p[id="email"]').text
        result_current_address = setup.find_element(By.CSS_SELECTOR, 'p[id="currentAddress"]').text
        result_permanent_address = setup.find_element(By.CSS_SELECTOR, 'p[id="permanentAddress"]').text

        output_board_data = [result_name == f'Name:{val_name}', result_email == f'Email:{val_email}',
                             result_current_address == f'Current Address :{val_current_address}',
                             result_permanent_address == f'Permananet Address :{val_permanent_address}']
        assert all(output_board_data)

    def test_validate_email_field(self, setup):

        email = setup.find_element(By.XPATH, EMAIL_XPATH)
        submit = setup.find_element(By.XPATH, SUBMIT_XPATH)

        email.send_keys('test@@com.ua')

        setup.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        time.sleep(5)

        validation_email_color = email.value_of_css_property('border')

        assert validation_email_color == '1px solid rgb(255, 0, 0)'












