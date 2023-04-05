from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
import json


class BookStorePage(object):
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_book_list_by_publisher(publisher):
        url = "https://demoqa.com/BookStore/v1/Books"
        response = requests.get(url)
        result = json.loads(response.text).get('books')
        book_info = {}
        book_list = []
        for i in result:
            for k, v in i.items():
                if k == "title" or k == 'author' or k == 'publisher':
                    book_info[k] = v
            if book_info['publisher'] == publisher:
                book_list.append(book_info)
        return book_list

    def get_title_of_page(self):
        title = self.driver.find_element(By.XPATH, '//div[@class="main-header"]').text
        return title

    def login_button_clicked(self):
        login_button = self.driver.find_element(By.XPATH, '//button[@id="login"]')
        login_button.click()
        return self.driver.current_url

    def sort_asc_table_data(self, column_tittle):
        column = self.driver.find_element(By.XPATH, f'//div[text()="{column_tittle}"]')
        column.click()
        sorted_data_asc = self.driver.find_element(By.XPATH, '//div[contains(@class, "-sort-asc")]')
        return sorted_data_asc

    def sort_desc_table_data(self, column_tittle):
        column = self.driver.find_element(By.XPATH, f'//div[text()="{column_tittle}"]')
        column.click()
        column.click()
        sorted_data_asc = self.driver.find_element(By.XPATH, '//div[contains(@class, "-sort-desc")]')
        return sorted_data_asc

    def get_picture_book_by_author(self, author_name):
        row_book = self.driver.find_element(By.XPATH, f'//div[text()="{author_name}"]')
        book_img = row_book.find_element(By.XPATH, '//ancestor::div[@role="row"]//img[@src]')
        return book_img.get_attribute('src')

    def search_books(self, search_text):
        search_box = self.driver.find_element(By.ID, "searchBox")
        search_box.clear()
        search_box.send_keys(search_text)

    def get_book_titles_by_search(self, search_text):
        self.search_books(search_text)
        book_titles = []
        book_list = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "app"))
        ).find_element(By.XPATH, '//div[@class = "rt-table"]')
        books = book_list.find_elements(By.XPATH, "//span[@class='mr-2']//a")
        for book in books:
            book_titles.append(book.text)
        if len(book_titles) == 0:
            raise ValueError(f"No books found for '{search_text}'")
        return book_titles
