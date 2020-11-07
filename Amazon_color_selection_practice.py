from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

COLOR_TAGS = ('Black', 'Burgundy', 'Caramel', 'Green', 'Navy', 'Yellow', 'Polka Dot Black', 'Polka Dot Coffee',
              'Polka Dot Green', 'Polka Dot Navy', 'Polka Dot Red', 'Polka Dot Yellow', 'Printed Geometry',
              'Printed Plaid', 'C-black', 'C-navy', 'Burgundy', 'C: Caramel', 'C: Green', 'C: Yellow', 'D-black',
              'D-green', 'D: Blue', 'D: Burgundy', 'D: Caramel', 'D: Navy', 'D: Yellow', 'Z: Caramel', 'C: Blue',
              'Z: Green', 'A: Blue', 'Z: Burgundy', 'Z: Black')
ALL_COLORS_SELECTION = (By.CSS_SELECTOR, "#variation_color_name li")
COLOR_CHOICE_NAME = (By.CSS_SELECTOR, "#variation_color_name span.selection")


# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.wait = WebDriverWait(driver, 10)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/product/B07PVB53RX/')

try:   # I use TRY and FINNALY just in case if one of the tests fail, the driver will close the window. So when I debug the program, I don't have to close many windows manually :)

    # find all elements of color selection
    driver.wait.until(EC.presence_of_all_elements_located(ALL_COLORS_SELECTION))
    colors = driver.find_elements(*ALL_COLORS_SELECTION)

    # verify amount of color tags matches amount of color choices
    assert len(COLOR_TAGS) == len(colors), f"Amount of pictures doesn't match the amount of color tags. Some are missing"

    # verify each color tag name matches each color choice from color selection
    for _ in range(len(colors)):
        colors[_].click()
        color_choice = driver.find_element(*COLOR_CHOICE_NAME)
        assert COLOR_TAGS[_] in color_choice.text, f"Colors don't match. Expected {COLOR_TAGS[_]}, but get {color_choice.text}"

finally:
    # close the window
    driver.quit()
