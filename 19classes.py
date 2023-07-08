# from copyreg import dispatch_table
from time import time
from turtle import position
from unicodedata import name

'''
OOP - Object and the Class - Class is the blueprint that the
object is the instance of the class.

A class is a blueprint for how something should be defined.
e.g. a form or questionnaire. An instance of a class is like
a form that has been filled out with infformation.

This is a stub for a class representing a house that can be
used to create objects and evaluate different metrics that we
may require in constructing it.
'''

class House:
    def __init__(self, room, bathroom):
        self.room = room
        self.bathroom = bathroom

    # Functionality to calculate the costs from the area of the house
    def cost_evaluation(self, rate):
        cost = rate * self.room
        return cost


house = House(5, 2)
house1 = House(4, 3)

print(house.room, house.bathroom)

house.room = 7
print(house.room)


## Instantiate a Custom Object
class Recipe():
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(f"The {self.dish} has {str(self.items)} and takes "
         f"{str(self.time)} mins to prepare" )


pizza = Recipe("Pizza", ["cheese", "bread", "tomatoe"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 30)

print(pizza.contents())



# Another
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(f"{philosopher} wrote the book: {book}")


whodid = MyFirstClass()
print(whodid.hand_list("Sun Tzu", "The Art of War"))



### Instance Methods
class Payslips():
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    
    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " +str(self.amount)
        else:
            return self.name + " is not paid yet"

nathan = Payslips("worla", "no", 200)
print(nathan.status())


### Inheritance
class Employee:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

class Supervisors(Employee):
    def __init__(self, first_name, last_name, password) -> None:
        super().__init__(first_name, last_name)
        self.password = password

class Chefs(Employee):
    def leave_request(self, days):
        return f"May i take a leave for {str(days)} days"


adrian = Supervisors("adrian", "A", "apple")
emily = Chefs("Emily", "E")
luno = Chefs("Luno", "L")

print(adrian.password)
print(emily.first_name)
print(emily.leave_request(5))


#Multiple inheritance
class E_names():
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

class E_details():
    def __init__(self, status, salary) -> None:
        self.status = status
        self.salary = salary

class Worker(E_names, E_details):
    def __init__(self, fname, lname) -> None:
        super().__init__(fname, lname)



## Abstract Classes and Methods
