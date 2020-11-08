from selenium.webdriver.common.by import By
from pages.base_page import Page


class HamburgerMenuPopUp (Page):

    AMAZON_MUSIC_LINK = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_LINKS = (By.CSS_SELECTOR, "ul.hmenu-translateX a[class=hmenu-item]")

    def click_amazon_music_menu_link(self):
        self.wait_for_element_click(self.AMAZON_MUSIC_LINK)


    def verify_amazom_music_links(self, number: int):
        self.wait_for_presence_off_all_elements(self.AMAZON_MUSIC_MENU_LINKS)
        self.verify_ammount_of_elements(number, *self.AMAZON_MUSIC_MENU_LINKS)


