from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_get_id(setup, get_id):
    element_id = get_id
    element_text = setup.find_element(By.ID, element_id).text
    assert element_text == 'This text has random Id'


def test_wait_for_enable_element(setup):
    enable_button = setup.find_element(By.ID, 'enableAfter')
    is_selected_enable_element(setup, 'enableAfter')
    assert enable_button.is_enabled()


def test_button_is_present(setup):
    setup.refresh()
    is_visible(setup, 'visibleAfter')
    enable_button = setup.find_element(By.ID, 'visibleAfter')
    assert enable_button.is_displayed()


def is_visible(setup, elem_id: str) -> Any:
    return WebDriverWait(setup, 6).until(ec.visibility_of_element_located((By.ID, elem_id)))


def is_selected_enable_element(setup, elem_id: str) -> Any:
    return WebDriverWait(setup, 6).until(ec.element_to_be_clickable((By.ID, elem_id)))





