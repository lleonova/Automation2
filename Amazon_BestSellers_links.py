from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

BESTSELLERS_ICON = (By.CSS_SELECTOR, "a[href*='bestsellers']")
BESTSELLERS_LINKS =(By.CSS_SELECTOR, "#zg_tabs li")

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

try:
    # click on BestSellers icon
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BESTSELLERS_ICON)).click()

    # verify that page has 5 links displayed
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(BESTSELLERS_LINKS))
    number_of_links = len(driver.find_elements(*BESTSELLERS_LINKS))
    assert number_of_links == 5, f'Expected 5 links, but got {number_of_links}'

finally:
    # close the window
    driver.quit()



