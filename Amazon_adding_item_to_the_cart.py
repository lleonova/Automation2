from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


INPUT_FIELD = (By.ID, "twotabsearchtextbox")
SEARCH_WORD = "Amoretu Women Summer Tunic Dress"
SEARCH_RESULTS_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SEARCH_RESULTS_ITEM = (By.CSS_SELECTOR, "div.s-result-item.sg-col-4-of-32")
DROP_DOWN_MENU_SIZE = (By.XPATH, "//select[@id='native_dropdown_selected_size_name']")
COLOR_CHOICE = (By.ID, "a-autoid-6-announce")
#DROP_DOWN_MENU_SIZE = (By.XPATH, "//select[@id='native_dropdown_selected_size_name']/option[@id='native_size_name_1']")
ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
CART_COUNT = (By.ID, "nav-cart-count")
ADDED_TO_CART = (By.CSS_SELECTOR, "h1")
SHOPPING_CART_BTN = (By.ID, "nav-cart")
ITEMS_IN_CART = (By.ID, "sc-subtotal-label-activecart")


# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# search for 'search word'
search = driver.find_element(*INPUT_FIELD)
search.clear()
search.send_keys(*SEARCH_WORD)
search.submit()

# click on the first item in the search result
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SEARCH_RESULTS_ITEM)).click()

try:
    # choose Small size from drop-down menu
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(DROP_DOWN_MENU_SIZE))
    select = Select(driver.find_element(*DROP_DOWN_MENU_SIZE))
    select.select_by_visible_text("Small")

    # choose first color choice
    driver.find_element(*COLOR_CHOICE).click()

    # click "Add to Cart" button
    WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(*ADD_TO_CART_BTN)))
    driver.find_element(By.ID, "add-to-cart-button").click()

    # verify an item is added to the cart
    cart_items_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CART_COUNT)).text
    assert int(cart_items_count) != 0, f'Expected 1 item in shopping cart, but got {cart_items_count}'

    added_to_cart_text = driver.find_element(*ADDED_TO_CART).text
    assert "Added to Cart" in added_to_cart_text

    # click the shopping cart button
    driver.find_element(*SHOPPING_CART_BTN).click()

    # verify the shopping cart has 1 item
    items_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ITEMS_IN_CART))
    assert "1 item" in items_in_cart.text, f'Expected 1 item in shopping cart page, but got {items_in_cart}'

finally:
    # close the window
    driver.quit()