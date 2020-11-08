from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
from pages.search_results_page import SearchResults
from pages.product_page import Product
from pages.cart_subtotal_page import CartSubtotal
from pages.shopping_cart_page import ShopCart
from pages.bestsellers_page import BestSellers
from pages.whole_foods_deals_page import WholeFoodsDeals
from pages.sign_in_page import SignIn
from pages.hamburger_menu_pop_up import HamburgerMenuPopUp

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
        self.whole_foods_deals_page = WholeFoodsDeals(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.hamburger_menu_pop_up = HamburgerMenuPopUp(self.driver)