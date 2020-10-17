from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartSubtotal(Page):

    ADDED_TO_CART = (By.CSS_SELECTOR, "h1")

    def verify_item_added_to_cart_text(self, message: str):
        self.verify_text(message, *self.ADDED_TO_CART)
