from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
from pages.search_results_page import SearchResults
from pages.product_page import Product
from pages.cart_subtotal_page import CartSubtotal
from pages.shopping_cart_page import ShopCart
from pages.bestsellers_page import BestSellers

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.product_page = Product(self.driver)
        self.cart_subtotal_page = CartSubtotal(self.driver)
        self.shopping_cart_page = ShopCart(self.driver)
        self.bestsellers_page = BestSellers(self.driver)
