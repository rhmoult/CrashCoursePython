pizzas = ['mushroom', 'vegetarian', 'sausage', 'pepperoni', 'meat lovers', 'hawaiian']

count = 1
really = 'really '

for pizza in pizzas:
    print(f"I {really}like {pizza} pizza.")
    really += "really "

print(f"I really, really, really like pizza!")