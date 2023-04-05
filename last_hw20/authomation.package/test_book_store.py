import pytest
import requests
from Book_Store_Page_Object import BookStorePage


class TestBookStore:

    @pytest.mark.parametrize('publisher', ["O'Reilly Media", 'No Starch Press',
                                           'abcd'])
    def test_book_list_by_publisher(self, setup_chrome, publisher):
        page = BookStorePage(setup_chrome)
        book_list = BookStorePage.get_book_list_by_publisher(publisher)
        assert len(book_list) == len(page.get_book_titles_by_search(publisher))

    @pytest.mark.parametrize('author', ['Nicholas C. Zakas', 'Richard E. Silverman', 'Glenn Block et al.',
                                        'Marijn Haverbeke', 'Eric Elliott'])
    def test_image_book(self, setup_chrome, author):
        page = BookStorePage(setup_chrome)
        img = page.get_picture_book_by_author(author)
        assert requests.get(img).status_code == 200

    def test_search_book(self, setup_chrome):
        page = BookStorePage(setup_chrome)
        book_list = page.get_book_titles_by_search("java")
        assert len(book_list) > 0

    def test_sorted_asc(self, setup_chrome):
        page = BookStorePage(setup_chrome)
        result = page.sort_asc_table_data("Publisher")
        assert "-sort-asc" in result.get_attribute("class")

    def test_login_page(self, setup_chrome):
        page = BookStorePage(setup_chrome)
        result = page.login_button_clicked()
        assert 'login' in result



