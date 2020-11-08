from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)


    def open_page(self, url=''):
        self.driver.get(self.base_url + url)


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def input(self, text,  *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)


    def wait_for_element_click(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(*locator)).click()


    def wait_for_element_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(*locator))


    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(*locator))


    def wait_for_presence_off_all_elements(self, *locator):
        self.driver.wait.until(EC.presence_of_all_elements_located(*locator))


    def wait_for_element_refresh(self, *locator):
        self.driver.wait.until(EC.staleness_of(self.driver.find_element(*locator)))
        self.driver.wait.until(EC.element_to_be_clickable(*locator))


    def verify_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'


    def choose_from_drop_down_menu_by_text(self, expected_text: str, *locator):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(expected_text)


    def verify_ammount_of_elements(self, number, *locator):
        number_of_elements = len(self.find_elements(*locator))
        assert int(number) == number_of_elements, f'Expected {number} elements, but got {number_of_elements}'


    # Verify string 'partial link' matches the part of current link
    def verify_partial_link(self, partial_link: str):
        link = self.driver.current_url
        assert partial_link in link, f"Expected to open Sign In page, but get {link}"

