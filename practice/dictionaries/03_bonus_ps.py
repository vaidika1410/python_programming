products = {
    "A": 5600,
    "B": 799,
    "C": 4499
}

max_price = max(products.values())

for product in products:
    if products[product] == max_price:
        print("product with highest price:", product)