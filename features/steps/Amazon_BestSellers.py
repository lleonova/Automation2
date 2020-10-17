from behave import given, then, when

@then('Click on BestSellers icon')
def click_on_link(context):
    context.app.top_nav_menu.click_bestsellers_link()

@then('Verify that page has {number} links displayed')
def number_of_links(context, number):
    context.app.bestsellers_page.verify_ammount_of_links(number)

