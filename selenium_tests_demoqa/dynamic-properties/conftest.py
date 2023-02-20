import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def get_url(get_webdriver):
    url = 'https://demoqa.com/dynamic-properties'
    yield url


@pytest.fixture(scope='function')
def get_id(setup):
    element = setup.find_element(By.XPATH, '//p[contains(text(), "random")]')
    yield element.get_attribute('id')





