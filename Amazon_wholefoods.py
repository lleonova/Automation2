from behave import given, then, when

@given('Open Amazon WholeFoods Deals page')
def open_amazon_wholefood_deals(context):
    context.app.page.open_page('wholefoodsdeals')

@then('Every product under the yellow line has has a text ‘Regular’ and a product name')
def verify_regular_and_product_name(context):
    context.app.whole_foods_deals_page.verify_every_product_has_regular_and_product_name()
