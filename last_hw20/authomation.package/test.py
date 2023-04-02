import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Book_Store_Page_Object import BookStorePage
#
#
# def test_books(setup_chrome):
#     driver = setup_chrome
#     column_name = "Publisher"
#     abc = driver.find_element(By.XPATH, '//div[@role="rowgroup"][1]//div[@role="gridcell"][4]').text
#     column = driver.find_element(By.XPATH, f'//div[text()="Publisher"]')
#     column.click()
#     sorted_data_asc = driver.find_element(By.XPATH, '//div[contains(@class, "-sort-asc")]')
#     sorted_data_desc = driver.find_element(By.XPATH, '//div[contains(@class, "-sort-desc")]')
#     if sorted_data_asc:
#         assert True
#     else:
#         column.click()
#         assert True
#     print(abc)
#
#
# #//div[@role="rowgroup"][1]//div[@role="gridcell"][4].text
# #//div[@role="rowgroup"][last()-2]//div[@role="gridcell"][4].text
# def test_sorting(self):
#     column_publisher = self.driver.find_element(By.XPATH, '//div[text()="Publisher"]')
#     column_publisher.click()
#     sorted_data_asc = self.driver.find_element(By.XPATH, '//div[contains(@class, "-sort-asc")]')
#     assert "-sort-asc" in sorted_data_asc.get_attribute("class")

class TestBookStore:

    def test_search_book(self, setup_chrome):
        page = BookStorePage(setup_chrome)
        author_list = page.get_book_titles_by_author("Axel")
        assert len(author_list) > 0

