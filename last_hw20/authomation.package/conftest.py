import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_options():
    options = Options()
    #options.add_argument('--headless')
    return options


@pytest.fixture
def get_chrome(get_options):
    options = get_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def setup_chrome(request, get_chrome):
    driver = get_chrome
    if request.cls is not None:
        request.cls.driver = driver
    driver.get('https://demoqa.com/books')
    yield driver
    driver.quit()
