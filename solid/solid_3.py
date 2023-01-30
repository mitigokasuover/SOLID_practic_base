class Animal:
    def __init__(self,attrs):
        self.attributes = attrs
    

    def eat(self):
        print("Ate some food!")
    

class Cat(Animal):
    def eat(self, amount = 0.1):
        if amount > 0.3:
            print("stop eat")
        else:
            print("give more food")


class Dog(Animal):
    def eat(self):
        print("give more food to dog")
    
pluto = Dog({"name": "Pluto", "age": 3})
goofy = Dog({"name": "Goofy", "age": 2})
buttons = Cat(("Mr. Buttons", 4))

animals = (pluto + goofy)

for animal in animals:
    if animal.attributes["age"] > 2:
        print(animal.attributes["name"])