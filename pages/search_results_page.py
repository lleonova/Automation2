from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResults(Page):

    RESULTS_INFO_TEXT = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")
    SEARCH_RESULTS_ITEM = (By.CSS_SELECTOR, "div.s-result-item.sg-col-4-of-32")

    def verify_found_results_text(self, search_word):
        self.verify_text(search_word, *self.RESULTS_INFO_TEXT)

    def click_first_item(self):
        self.wait_for_element_click(*self.SEARCH_RESULTS_ITEM)
