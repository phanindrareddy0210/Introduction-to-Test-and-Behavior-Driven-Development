Feature: Manage Products

  Scenario: Create a new product
    When I create a product with "Laptop", "Electronics", and "True"
    Then the product is created

  Scenario: List all products
    When I request the list of products
    Then I see all products

  Scenario: Update a product
    When I update product 1 with "Updated Laptop"
    Then the product is updated

  Scenario: Delete a product
    When I delete product 1
    Then the product is deleted

  Scenario: Search by name
    When I search for products by name "Laptop"
    Then I see products with "Laptop"
