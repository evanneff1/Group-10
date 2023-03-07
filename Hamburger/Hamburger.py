# Group 10 Hamburger Project
# Evan Neff, Dawson Newell, Jake Millet, Tanner Child, Cameron Pennock, Paxton Davis
#we used git when completing this assignment

import random

#create an order class with variable burger_count and method randomBurgers
class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):
        return random.randint(1, 20)

#Create a person class with variable customer_name and method randomName(from a list of names)
class Person():
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander",
                            "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        randnumber = random.randint(0, 8)
        return self.asCustomers[randnumber]

#create a customer class, that calls the parent(person) constructor and has a variable order(order object)
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

#initialize the queue and dictionary
#queue = add to back and pop from front
#dictionary = keys(string): values(integers)
queue = []
Dict = {}

#create 100 customers and add them to the queue
for customer in range(0, 100):
    queueCustomer = Customer()

    queue.append(queueCustomer)

#while there are people in the queue, see if that person is in the dictionary. If they are, increment their number of burgers
#if they are not in the dictionary, add them to the dictionary
while len(queue):
    if queue[0].customer_name in Dict:
        TotalBurgers = Dict[queue[0].customer_name] 
        Dict[queue[0].customer_name] = TotalBurgers + queue[0].order.burger_count
        queue.pop(0)
    else:
        Dict[f"{queue[0].customer_name}"] = queue[0].order.burger_count
        queue.pop(0)

#sort the customers in a list
listSortedCustomers = sorted(Dict.items(), key=lambda x: x[1], reverse=True) 

#print out the customers in a sorted order
for Dasher in listSortedCustomers:
    print(f"{Dasher[0].ljust(19) }: {Dasher[1]}")
