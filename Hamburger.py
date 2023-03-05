# Group 10 Hamburger Project
# Evan Neff, Dawson Newell, Jake Millet, Tanner Child, Cameron Pennock, Paxton Davis

import random


class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):
        return random.randint(1, 20)


class Person():
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander",
                            "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        randnumber = random.randint(0, 8)
        return self.asCustomers[randnumber]


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

queue = []
Dict = {}

for i in range(0, 100):
    queueCustomer = Customer()

    queue.append(queueCustomer)

while len(queue):
    if queue[0].customer_name in Dict:
        TotalBurgers = Dict[queue[0].customer_name] 
        Dict[queue[0].customer_name] = TotalBurgers + queue[0].order.burger_count
        queue.pop(0)
    else:
        Dict[f"{queue[0].customer_name}"] = queue[0].order.burger_count
        queue.pop(0)

listSortedCustomers = sorted(Dict.items(), key=lambda x: x[1], reverse=True) 

for Dasher in listSortedCustomers:
    print(f"{Dasher[0]}: {Dasher[1]}")

