import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    #options.add_argument('--headless') #Use --headless if you don't need browser UI
    options.add_argument('--window-size=1080,1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def setup(request, get_webdriver, get_url):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(get_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def start_end_test():
    print('\nSTART TEST')
    yield
    print('\nEND TEST')
