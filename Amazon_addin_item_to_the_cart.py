from behave import given, then, when

@given('Open Amazon page')
def open_amazon(context):
    context.app.page.open_page()

# Perform search for the product
@when('Input {item} into search field')
def item_search(context, item):
    context.app.top_nav_menu.search_word(item)

@when('Click on search icon')
def click_search_icon(context):
    context.app.top_nav_menu.click_search_icon()

# Verify the corect search results are shown
@then('Product results for {item} are shown')
def verify_search_results(context, item):
    context.app.search_results_page.verify_found_results_text(item)

# Choose first item in the search results
@then('Click on first item in the search result')
def select_item(context):
    context.app.search_results_page.click_first_item()

# Select size
@then('Choose {value} size from drop-down menu')
def select_size(context, value):
    context.app.product_page.choosing_size(value)

# Select color
@then('Select first color choice')
def color_choise(context):
    context.app.product_page.choosing_color()

# Add to cart
@then('Click Add To Cart Button')
def add_to_cart(context):
    context.app.product_page.click_add_to_cart_btn()

# Verify the item was added to the cart
@then('Amazon Shopping Cart Count has {number} items')
def verify_shoping_cart_item_count(context, number):
    context.app.top_nav_menu.shopping_cart_counter(number)

@then('User can see {message} text')
def verify_added_to_cart_text(context, message):
    context.app.cart_subtotal_page.verify_item_added_to_cart_text(message)

# Go to Shopping Cart page
@then('Click on Shopping Cart icon')
def shopping_cart_icon_click(context):
    context.app.top_nav_menu.click_shopping_cart_icon()

# Verify the item was added to the cart
@then('Verify that cart has {many} item')
def items_in_shopping_cart(context, many):
    context.app.shopping_cart_page.verify_items_in_cart(many)

@then("Verify '{phrase}' text is present")
def verify_text_present(context, phrase: str):
    context.app.shopping_cart_page.verify_text_present(phrase)







