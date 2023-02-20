import pytest


@pytest.fixture
def get_url(get_webdriver):
    url = 'https://demoqa.com/radio-button'
    yield url
