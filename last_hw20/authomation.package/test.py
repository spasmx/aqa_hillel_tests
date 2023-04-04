import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Book_Store_Page_Object import BookStorePage
#
#

#
#
# #//div[@role="rowgroup"][1]//div[@role="gridcell"][4].text
# #//div[@role="rowgroup"][last()-2]//div[@role="gridcell"][4].text
# def test_sorting(self):
#assert "-sort-asc" in sorted_data_asc.get_attribute("class")
#     assert "-sort-asc" in sorted_data_asc.get_attribute("class")

class TestBookStore:

    def test_search_book(self, setup_chrome):
        page = BookStorePage(setup_chrome)
        author_list = page.get_book_titles_by_search("00000000")
        assert len(author_list) > 0

    def test_image_book(self,setup_chrome):
        page = BookStorePage(setup_chrome)
        img = page.get_picture_book_by_author('Addy Osmani')
        print(img)

    def test_sorted_asc(self, setup_chrome):
        page = BookStorePage(setup_chrome)
        result = page.sort_asc_table_data()
        assert "-sort-asc" in result

    def test_login_page(self, setup_chrome):
        page = BookStorePage(setup_chrome)
        result = page.login_button_clicked()
        print(result)


