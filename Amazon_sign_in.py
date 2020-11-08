from behave import given, then, when

@when('Click Return and Orders link')
def click_sign_in_link(context):
    context.app.top_nav_menu.click_return_and_orders_link()

@then('Verify Sign In page is opened')
def verify_sign_in_opened(context):
    context.app.sign_in_page.verify_sign_in_opened()

