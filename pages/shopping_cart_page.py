from selenium.webdriver.common.by import By
from pages.base_page import Page

class ShopCart(Page):

    NUMBER_ITEMS_IN_CART = (By.ID, "sc-subtotal-label-activecart")

    def verify_items_in_cart(self, number):
        self.wait_for_element_appear(*self.NUMBER_ITEMS_IN_CART)
        self.verify_text(number, *self.NUMBER_ITEMS_IN_CART)
