from behave import given

@given('the database is empty')
def step_impl(context):
    context.products = []
