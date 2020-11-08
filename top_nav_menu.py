from selenium.webdriver.common.by import By
from pages.base_page import Page

class TopNavMenu(Page):

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.CSS_SELECTOR, "span[id=nav-search-submit-text] input.nav-input")
    ITEMS_IN_THE_CART = (By.ID, "nav-cart-count")
    CART_ICON = (By.ID, 'nav-cart')
    BESTSELLERS_ICON = (By.CSS_SELECTOR, "a[href*='bestsellers']")
    RETURN_AND_ORDERS_LINK = (By.ID, "nav-orders")
    HAMBURGER_MENU_ICON = (By.ID, "nav-hamburger-menu")


    def search_word(self, search_word):
        self.input(search_word, *self.SEARCH_INPUT)


    def click_search_icon(self):
        self.click(*self.SEARCH_SUBMIT)


    def shopping_cart_counter(self, amount):
        self.verify_text(amount, *self.ITEMS_IN_THE_CART)


    def click_shopping_cart_icon(self):
        self.click(*self.CART_ICON)


    def click_bestsellers_link(self):
        self.click(*self.BESTSELLERS_ICON)


    def click_return_and_orders_link(self):
        self.click(*self.RETURN_AND_ORDERS_LINK)


    def click_hamburger_menu(self):
        self.wait_for_element_click(self.HAMBURGER_MENU_ICON)


