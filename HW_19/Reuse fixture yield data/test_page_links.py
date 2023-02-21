import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('get_webdriver_chrome')
class TestPageLinks:

    def test_links_home(self):
        links_home = self.driver.find_elements(By.XPATH, '//div[@id = "linkWrapper"]//a[text()="Home"]')
        assert len(links_home) == 2
