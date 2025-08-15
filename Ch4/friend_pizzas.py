pizzas = ['mushroom', 'vegetarian', 'sausage', 'pepperoni', 'meat lovers', 'hawaiian']

def printPizzaStatements(pizza_list, who="I", second_person_singular=False, really='really '):
    for pizza in pizza_list:
        if second_person_singular:
            like = "likes"
        else:
            like = "like"
        print(f"{who} {really}{like} {pizza} pizza.")
        really += "really "
    print(f"{who} really, really, really {like} pizza!")

printPizzaStatements(pizzas)


friend_pizzas = pizzas[:]
friend_pizzas.append('anchovy')

printPizzaStatements(friend_pizzas, who="My friend", second_person_singular=True)