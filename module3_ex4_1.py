import json

data_pizza = {"margarita": 400, "carbonara": 500}
with open("pizza.json", "w") as f:
    json.dump(data_pizza, f)


def add_pizza(name, price):
    with open("pizza.json", "r") as f:
        data_pizza = json.load(f)
    if name not in data_pizza:
        data_pizza[name] = price
        with open("pizza.json", "w") as f:
            json.dump(data_pizza, f)
    else:
        print("Пицца с таким именем уже существует")


def del_pizza(name):
    with open("pizza.json", "r") as f:
        data_pizza = json.load(f)
    if name in data_pizza:
        del data_pizza[name]
        with open("pizza.json", "w") as f:
            json.dump(data_pizza, f)
    else:
        print("Пиццы с таким именем не существует")


def order_pizza():
    with open("pizza.json", "r") as f:
        data_pizza = json.load(f)
    order = []
    cost = 0
    while True:
        q1 = input("Continue?")
        if q1 == "no":
            break
        pizza_name = input()
        if pizza_name in data_pizza.keys():
            order.append(pizza_name)
            cost += data_pizza[pizza_name]
            print("Pizza added")
    return {"order": order, "cost": cost}


while True:
    break_point = input("Stop?")
    if break_point == "yes":
        break
    chose_role = input("Chose role?")
    if chose_role == "user":
        print(order_pizza())
    else:
        q2 = input("Add or delete")
        if q2 == "del":
            del_pizza(input("Pizza name"))
        elif q2 == "add":
            add_pizza(input("Pizza name?"), int(input("Price?")))
