from selenium.webdriver.common.by import By
from pages.base_page import Page

class Product(Page):

    DROP_DOWN_MENU_SIZE = (By.CSS_SELECTOR, "select#native_dropdown_selected_size_name")
    COLOR_CHOICE = (By.ID, "a-autoid-9-announce")
    #COLOR_CHOICE = (By.CSS_SELECTOR, "button.a-button-text")
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    # Every time I ran this program, I have to double check the order of tags. Amazon keeps changing the colors :)
    COLOR_TAGS = ('Black', 'Blue', 'Burgundy', 'Caramel', 'Green', 'Navy', 'Yellow', 'Polka Dot Black', 'B: Polka Dot Coffee',
                  'Polka Dot Green', 'Polka Dot Navy', 'Polka Dot Red', 'Polka Dot Yellow', 'Printed Geometry',
                  'Printed Plaid', 'C-black', 'C-navy', 'Blue', 'Burgundy', 'C: Caramel', 'C: Green', 'C: Yellow', 'D-black',
                  'D-green', 'D: Blue', 'D: Burgundy', 'D: Caramel', 'D: Navy', 'D: Yellow', 'Z: Caramel',
                  'Z: Green', 'Z: Burgundy', 'Z: Black')
    ALL_COLORS_SELECTION = (By.CSS_SELECTOR, "#variation_color_name li")
    COLOR_CHOICE_NAME = (By.CSS_SELECTOR, "#variation_color_name span.selection")


    colors = []


    def choosing_size(self, value):
        self.wait_for_element_appear(self.DROP_DOWN_MENU_SIZE)
        self.choose_from_drop_down_menu_by_text(value, *self.DROP_DOWN_MENU_SIZE)


    def choosing_color(self):
        self.wait_for_element_click(self.COLOR_CHOICE)
        #list_of_colors = self.find_elements(*self.COLOR_CHOICE)
        # print(list_of_colors)
        # print(len(list_of_colors))
        #list_of_colors[3].click() # the actual product colors starts from 4th position


    def click_add_to_cart_btn(self):
        self.wait_for_element_refresh(self.ADD_TO_CART_BTN)
        self.click(*self.ADD_TO_CART_BTN)


    def verify_number_dress_colors(self):
        self.wait_for_presence_off_all_elements(self.ALL_COLORS_SELECTION)
        self.colors = self.find_elements(*self.ALL_COLORS_SELECTION)
        assert len(self.COLOR_TAGS) == len(self.colors), f"Amount of pictures doesn't match the amount of color tags. Some are missing"


    def verify_dress_colors(self):
        for _ in range(len(self.colors)):
            self.colors[_].click()
            color_choice = self.find_element(*self.COLOR_CHOICE_NAME)
            assert self.COLOR_TAGS[_] in color_choice.text, f"Colors don't match. Expected {self.COLOR_TAGS[_]}, but get {color_choice.text}"

