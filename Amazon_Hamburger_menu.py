from behave import when, then


@when('Click on the Hamburger menu')
def click_hamburger_menu(context):
    context.app.top_nav_menu.click_hamburger_menu()


@when('Click on Amazon Music link in Hamburger menu')
def click_menu_item(context):
    context.app.hamburger_menu_pop_up.click_amazon_music_menu_link()


@then('{number} menu items are present')
def verify_amazom_music_links(context, number):
    context.app.hamburger_menu_pop_up.verify_amazom_music_links(number)