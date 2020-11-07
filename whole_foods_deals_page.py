from selenium.webdriver.common.by import By
from pages.base_page import Page

class WholeFoodsDeals(Page):
    PRODUCTS_UNDER_YELLOW_LINE = (By.CSS_SELECTOR, "#wfm-pmd_deals_section div.wfm-desktop-section-size:nth-of-type(6) li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")

    def verify_every_product_has_regular_and_product_name(self):
        # find all products under yellow line
        self.wait_for_presence_off_all_elements(self.PRODUCTS_UNDER_YELLOW_LINE)
        products = self.find_elements(*self.PRODUCTS_UNDER_YELLOW_LINE)

        for item in products:
            # verify every product on the page has a text ‘Regular’
            assert "Regular" in item.text, f"Expected 'Regular' in product price, but get {item.text}"

            # verify every product on the page has a product name
            assert item.find_element(*self.PRODUCT_NAME), f"Expected every product on the page has a product name, but didn't find it"
