favorite_pizzas = ['classic', 'smoked', 'pineapple']
friends_pizzas = favorite_pizzas[:]

favorite_pizzas.append('pasta')
friends_pizzas.append('cheese')

print("My favorite pizzas:")
for pizza in favorite_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas:")
for pizza in friends_pizzas:
    print(pizza)
