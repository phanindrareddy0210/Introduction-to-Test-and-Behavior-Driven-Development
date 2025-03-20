from behave import when, then

@when('I create a product with "{name}", "{category}", and "{available}"')
def step_impl(context, name, category, available):
    context.products.append({
        "name": name,
        "category": category,
        "available": available.lower() == "true"
    })

@when('I request the list of products')
def step_impl(context):
    context.response = context.products

@when('I update product 1 with "{name}"')
def step_impl(context, name):
    context.products[0]["name"] = name

@when('I delete product 1')
def step_impl(context):
    context.products.pop(0)

@when('I search for products by name "{name}"')
def step_impl(context, name):
    context.response = [p for p in context.products if name in p["name"]]

@then('the product is created')
def step_impl(context):
    assert len(context.products) == 1

@then('I see all products')
def step_impl(context):
    assert len(context.response) > 0

@then('the product is updated')
def step_impl(context):
    assert context.products[0]["name"] == "Updated Laptop"

@then('the product is deleted')
def step_impl(context):
    assert len(context.products) == 0

@then('I see products with "{name}"')
def step_impl(context, name):
    assert any(name in p["name"] for p in context.response)
