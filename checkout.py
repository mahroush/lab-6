def calculate_total(price, quantity, discount=0):
    subtotal = price * quantity
    return subtotal - discount

price = 10
quantity = 3
discount = 5

total = calculate_total(price, quantity, discount)

print("Total:", total)
