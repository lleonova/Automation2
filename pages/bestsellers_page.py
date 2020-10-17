from selenium.webdriver.common.by import By
from pages.base_page import Page

class BestSellers(Page):

    BESTSELLERS_LINKS = (By.CSS_SELECTOR, "#zg_tabs li")

    def verify_ammount_of_links(self, number):
        self.verify_ammount_of_elements(number, *self.BESTSELLERS_LINKS)

