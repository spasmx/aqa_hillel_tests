import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_chrome_headless():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def get_webdriver_chrome(request, get_chrome_headless):
    driver = get_chrome_headless
    if request.cls is not None:
        request.cls.driver = driver
    driver.get('https://demoqa.com/links')
    yield
    driver.quit()
