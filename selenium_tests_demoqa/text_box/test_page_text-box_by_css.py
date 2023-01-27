from .locators_сss import *
from selenium.webdriver.common.by import By


class TestPageTextBox:

    def test_output_data_on_fields_xpath(self, setup):

        full_name_field = setup.find_element(By.CSS_SELECTOR, FULL_NAME_CSS)
        email_field = setup.find_element(By.CSS_SELECTOR, EMAIL_CSS)
        current_address_field = setup.find_element(By.CSS_SELECTOR, CURRENT_ADDRESS_CSS)
        permanent_address_field = setup.find_element(By.CSS_SELECTOR, PERMANENT_ADDRESS_CSS)
        submit_button = setup.find_element(By.CSS_SELECTOR, SUBMIT_CSS)

        full_name_field.send_keys('Sergey')
        email_field.send_keys('test@email.com')
        current_address_field.send_keys('test current address')
        permanent_address_field.send_keys('test permanent address')

        val_name = full_name_field.get_attribute('value')
        val_email = email_field.get_attribute('value')
        val_current_address = current_address_field.get_attribute('value')
        val_permanent_address = permanent_address_field.get_attribute('value')

        setup.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        result_name = setup.find_element(By.CSS_SELECTOR, 'p[id="name"]').text.split(':')[1]
        result_email = setup.find_element(By.CSS_SELECTOR, 'p[id="email"]').text.split(':')[1]
        result_current_address = setup.find_element(By.CSS_SELECTOR, 'p[id="currentAddress"]').text.split(':')[1]
        result_permanent_address = setup.find_element(By.CSS_SELECTOR, 'p[id="permanentAddress"]').text.split(':')[1]

        output_board_data = [result_name == val_name, result_email == val_email,
                             result_current_address == val_current_address,
                             result_permanent_address == val_permanent_address]
        assert all(output_board_data)

    def test_validate_email_field(self, setup):

        email = setup.find_element(By.CSS_SELECTOR, EMAIL_CSS)
        submit = setup.find_element(By.CSS_SELECTOR, SUBMIT_CSS)

        email.send_keys('test@@com.ua')

        setup.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        validation_email_color = setup.find_element(By.CSS_SELECTOR, '#userEmail.field-error')

        assert validation_email_color
