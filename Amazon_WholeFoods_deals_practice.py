from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PRODUCTS_UNDER_YELLOW_LINE = (By.CSS_SELECTOR, "#wfm-pmd_deals_section div.wfm-desktop-section-size:nth-of-type(6) li")
PRODUCT_NAME = (By.CSS_SELECTOR, "span.wfm-sales-item-card__product-name")

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.wait = WebDriverWait(driver, 10)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/wholefoodsdeals')

try:   # I use TRY and FINNALY just in case if one of the tests fail, the driver will close the window. So when I debug the program, I don't have to close many windows manually :)

    # find all products under yellow line
    driver.wait.until(EC.presence_of_all_elements_located(PRODUCTS_UNDER_YELLOW_LINE))
    products = driver.find_elements(*PRODUCTS_UNDER_YELLOW_LINE)

    for item in products:
        # verify every product on the page has a text ‘Regular’
        assert "Regular" in item.text, f"Expected 'Regular' in product price, but get {item.text}"

        # verify every product on the page has a product name
        assert item.find_element(*PRODUCT_NAME), f"Expected every product on the page has a product name, but didn't find it"

finally:
    # close the window
    driver.quit()