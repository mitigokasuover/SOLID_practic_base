class Creature:
    def __init__(self, name):
        self.name = name
    

class SwimmerInterface:
    def swim(self):
        pass

class WalkerInterface:
    def walk(self):
        pass

class TalkerInterface:
    def talk(self):
        pass


class Human(Creature, SwimmerInterface, WalkerInterface, TalkerInterface):
    def __init__(self, name):
        super().__init__(name)
    

    def swim(self):
        print(f"I'm {self.name} and i can swim")
        
    
    def walk(self):
        print(f"I'm {self.name} and i can walk")


    def talk(self):
        print(f"I'm {self.name} and i can talk")


class Fish(Creature, SwimmerInterface):
    def __init__(self, name):
        super().__init__(name)

    
    def swim(self):
        print(f"I'm {self.name} and I can swim")

class Cat(Creature, SwimmerInterface, WalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    
    def swim(self):
        print(f"I'm {self.name} and i can swim")
    

    def walk(self):
        print(f"I'm {self.name} and i can walk")


human = Human("john doe")
human.swim()
human.walk()
human.talk()

fish = Fish("Nemo")
fish.swim()

cat = Cat("mr. Buttons")
cat.walk()
cat.swim()
