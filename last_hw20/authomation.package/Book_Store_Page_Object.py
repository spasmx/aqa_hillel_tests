import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures('setup_chrome')
class BookStorePage:
    def __init__(self, driver):
        self.driver = driver

    def search_books(self, search_text):
        search_box = self.driver.find_element(By.ID, "searchBox")
        search_box.clear()
        search_box.send_keys(search_text)
        search_button = self.driver.find_element(By.ID, "searchBooks")
        search_button.click()

    def search_books_by_author(self, author_name):
        search_box = self.driver.find_element(By.ID, "searchBox")
        search_box.clear()
        search_box.send_keys(author_name)
        search_button = self.driver.find_element(By.ID, "searchBooks")
        search_button.click()

    def get_book_titles_by_author(self, author_name):
        self.search_books_by_author(author_name)
        book_titles = []
        book_list = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "app"))
            ).find_element(By.XPATH, '//div[@class = "rt-table"]')
        books = book_list.find_elements(By.XPATH, "//span[@class='mr-2']//a")
        for book in books:
            book_titles.append(book.text)
        if not book_titles:
            raise ValueError(f"No books found for author '{author_name}'")
        return book_titles


class TestBookStore:

    def test_search_book(self, setup_chrome):
        page = BookStorePage(setup_chrome)
        author_list = page.get_book_titles_by_author("s")

        print(author_list)
        #assert len(author_list) > 0
