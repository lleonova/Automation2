from selenium import webdriver
from selenium.webdriver.common.by import By

INPUT_FIELD = (By.ID, "twotabsearchtextbox")
SEARCH_WORD = "Pants"
SEARCH_RESULTS_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SEARCH_RESULTS_ITEM = (By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")

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


# verify search result
result_text = driver.find_element(*SEARCH_RESULTS_TEXT).text
result_item = driver.find_element(*SEARCH_RESULTS_ITEM).text

assert SEARCH_WORD in result_text, f'Expected search result for {SEARCH_WORD}, but got {result_text}'
assert SEARCH_WORD in result_item, f'Expected search result for {SEARCH_WORD}, but got {result_item}'


# close the window
driver.quit()