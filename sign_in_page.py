from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignIn(Page):

    SIGN_IN_TEXT = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def verify_sign_in_opened(self):
        self.verify_text('Sign-In', *self.SIGN_IN_TEXT)



