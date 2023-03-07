# Group 10 Hamburger Project
# Evan Neff, Dawson Newell, Jake Millet, Tanner Child, Cameron Pennock, Paxton Davis


# THIS IS FOR TESTING

import random


class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):
        self.number_of_burgers = random.randint(1, 20)
        return self.number_of_burgers


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


queue = Customer()

testOrder = Order()
testName = Person()

print(testOrder.burger_count)
print(testName.customer_name)
