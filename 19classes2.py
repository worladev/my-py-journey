#MORE ON CLASSES

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0 #why
    
    def accelerate(self):
        self.speed = self.speed + 10
        return f"The {self.make} is now going {self.speed} mph."
    
    def brake(self):
        self.speed = self.speed - 10
        return f"The {self.make} is now going {self.speed} mph."


toyota = Car("Toyota", "Corolla", 1990)
kia = Car("Kia", "forte", 2000)

print(toyota.accelerate())
print(toyota.brake())

print(kia.accelerate())
print(kia.brake())


class Electric_Car(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
    
    def charge_battery(self, percentage):
        self.battery_size = self.battery_size + percentage
        print(f"The current battery is now charged to {self.battery_size} %")
    
    def accelerate(self):
        self.speed = self.speed + 50
        return f"The {self.make} is now going {self.speed} mph"
    
    def brake(self):
        self.speed = self.speed - 50
        return f"The {self.make} is now going {self.speed} mph."


toyota = Car("Toyota", "camry", 2023)
print(toyota.accelerate())
print(toyota.brake())
print(toyota.make)

tesla = Electric_Car("Tesla", "Model Y", 2023, 20)
print(tesla.accelerate())
print(tesla.brake())
print(tesla.make)


####The Object and The Class
# The Object is the instance of the class 
# Class is the blueprint that the object get's instantiated from.

# When we were using the list:
# list(), set(), tuple() and dict()
numbers = []
numbers2 = list()
print(type(numbers2))
string = "Hello World"
string2 = ["Hello World"]

# Number -> integer, float, complex
# String
# Boolean

class Simplest:
  pass

sim = Simplest()
sim2 = Simplest()
print(sim)
print(dir(sim))
print(type(sim) is Simplest)
print(type(sim2) is Simplest)
print(type(sim))


# Class Variable & Instance Variable
class Redolf:
  species = "Human"
  age = 23 # This is a class variable

person = Redolf()
person1 = Redolf()
# print(Redolf.species)
print(Redolf.age)
# Redolf.alive = True # Class Variable -> is dynamically added to the class
# print(Redolf.alive)
person.alive = True # instance variable
person.color = "Black"
print(person.alive)
print(person.color)
print(person1.species)
print(person1.age)
print(person.age)
# print(Redolf.alive)


class Person:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def walking(self):
        return f'{self.name} is walking to school.'

redolf = Person("Redolf", 23, "fair") # instantiating a class or Creating an object from the Person class
print(redolf.name)
print(redolf.age)
print(redolf.color)

redolf.walking()


### Another example epanding on using instance variable
class Price:
  
  # def __init__(self, net_price):
  #   self.net_price = net_price

  def final_price(self, vat , discount=0):
    return (self.net_price * (100 / vat) / 100) - discount


p1 = Price()
p1.net_price = 115
print(p1.final_price(20, 10))


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b

    @staticmethod
    def display(s):
        return s.upper()

rect = Rectangle(12, 12)
print(rect.area())
print(rect.display("mary is a"))


### Inheritance in Object-Oriented Programming
class Person:
  def __init__(self, name, age, color):
    self.name = name
    self.age = age
    self.color = color

  def walking(self):
    return f'{self.name} is walking to school.'


redolf = Person("Redolf", 23, "fair")
redolf.walking()

class Mary(Person):
  def walking(self):
    return f"{self.name} is now walking to school"
  

mary = Mary("Mary", 21, "fair")
mary.walking()


### Another example of class inheritance
class Engine:
  def start(self):
    return "Engine has atarted"

  def stop(self):
    return "Engine has stopped"


class ElectricCar(Engine):
  pass

class V8Engine(Engine):
  pass

e = ElectricCar()
e.start()
