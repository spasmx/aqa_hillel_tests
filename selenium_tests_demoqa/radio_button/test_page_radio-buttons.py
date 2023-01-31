from .locators import *
from selenium.webdriver.common.by import By


def test_activate_yes_radio_is_selected(setup):
    label_yes_radiobutton = setup.find_element(By.XPATH, LABEL_YES_RADIOBUTTON)
    yes_radio_button = setup.find_element(By.XPATH, INPUT_YES_RADIOBUTTON)
    label_yes_radiobutton.click()
    assert yes_radio_button.is_selected()


def test_activate_yes_radio_from_results_text(setup):
    label_yes_radiobutton = setup.find_element(By.XPATH, LABEL_YES_RADIOBUTTON)
    label_yes_radiobutton.click()

    result_text = setup.find_element(By.CSS_SELECTOR, 'span.text-success').text
    assert 'Yes' == result_text


def test_get_radio_buttons_info(setup):
    radio_button_info = {}
    all_radiobutton = setup.find_element(By.XPATH, '//div[contains(@class, "custom-control")]/..')
    labels_radiobutton = all_radiobutton.find_elements(By.XPATH, '//label[@for]')
    inputs_radiobutton = all_radiobutton.find_elements(By.XPATH, '//input[@type="radio"]')

    for radio in list(range(len(labels_radiobutton))):
        radio_button_info[labels_radiobutton[radio].text] = {'Selected': inputs_radiobutton[radio].is_selected(),
                                                             'Enabled': inputs_radiobutton[radio].is_enabled()}

    print(radio_button_info)
    return radio_button_info


def test_activate_disabled_radio_button(setup):
    label_no_radiobutton = setup.find_element(By.XPATH, LABEL_NO_RADIOBUTTON)
    input_no_radiobutton = setup.find_element(By.XPATH, INPUT_NO_RADIOBUTTON)
    setup.execute_script("arguments[0].removeAttribute('disabled','disabled')", input_no_radiobutton)
    label_no_radiobutton.click()
    assert input_no_radiobutton.is_selected()
