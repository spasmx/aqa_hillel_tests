from selenium.webdriver.common.by import By


def test_get_id(setup, get_id):
    element_id = get_id
    element_text = setup.find_element(By.ID, element_id).text
    assert element_text == 'This text has random Id'


def test_wait_for_enable_element(setup):
    pass


def test_button_is_present(setup):
    pass

