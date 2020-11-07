from behave import given, then, when

@given('Open Amazon product {number} page')
def open_amazon(context, number):
    context.app.page.open_page(f'gp/product/{number}/')


@when('Confirm number of Dress color choices')
def number_of_colors(context):
    context.app.product_page.verify_number_dress_colors()

@then('Verify User can select trough Dress colors')
def verify_dress_colors(context):
    context.app.product_page.verify_dress_colors()