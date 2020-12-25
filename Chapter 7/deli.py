sandwich_orders = ['veg sandwich', 'cheese sandwich', 'chicken sandwich', 'chinese sandwich']

finshed_orders = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"We have finished making your {sandwich.title()}.")
    finshed_orders.append(sandwich)

print("\nHere are the finished orders:")
for order in finshed_orders:
    print(order.title())
