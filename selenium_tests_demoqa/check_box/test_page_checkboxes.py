from .locators import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_click_check_box(setup):
    assert click_checkbox(setup, ['commands', 'general'])


def click_checkbox(setup, checkboxes: list):
    check_clicking = []
    while len(check_clicking) != len(checkboxes):
        try:
            for toggle, xpath in TOGGLE_BUTTON.items():
                toggle_button = setup.find_element(By.XPATH, xpath)
                setup.execute_script("arguments[0].scrollIntoView();", toggle_button)
                toggle_button.click()
                TOGGLE_BUTTON.pop(toggle)
                for elem in checkboxes:
                    checkbox = setup.find_element(By.XPATH, f'//span[@class = "rct-checkbox"]'
                                                            f'[ancestor::label[@for = "tree-node-{elem}"]]')
                    input_folder = setup.find_element(By.XPATH, f'//input[@id="tree-node-{elem}"]')
                    setup.execute_script("arguments[0].scrollIntoView();", checkbox)
                    if not input_folder.is_selected():
                        checkbox.click()
                        check_clicking.append(input_folder.is_selected())
        except NoSuchElementException:
            pass
        except RuntimeError:
            break
    return all(check_clicking)








