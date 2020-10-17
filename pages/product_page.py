from selenium.webdriver.common.by import By
from pages.base_page import Page

class Product(Page):

    DROP_DOWN_MENU_SIZE = (By.CSS_SELECTOR, "select#native_dropdown_selected_size_name")
    COLOR_CHOICE = (By.ID, "a-autoid-6-announce")
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    def choosing_size(self, value):
        self.wait_for_element_appear(*self.DROP_DOWN_MENU_SIZE)
        self.choose_from_drop_down_menu(value, *self.DROP_DOWN_MENU_SIZE)

    def choosing_color(self):
        list_of_colors = self.find_elements(*self.COLOR_CHOICE)
        list_of_colors[0].click()

    def click_add_to_cart_btn(self):
        self.wait_for_element_not_stale(*self.ADD_TO_CART_BTN)
        self.find_element(*self.ADD_TO_CART_BTN).click()

