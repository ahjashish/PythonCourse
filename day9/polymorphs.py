class Player():
    def signed_in(self):
        print("User is logged in.")

    def attack(self):
        print("Do nothing.")


class Wizard(Player):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        Player.attack(self)  # Just a way to use parent class method.
        print(f"{self.name} is attacking with {self.power} power.")


class Archer(Player):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f"{self.name} is attacking with {self.arrow} arrows.")


class HybridSoldier(Player):
    def attack(self):
        print("Hybrid Soldier is attacking with new power")


wizard1 = Wizard("John", 50)
archer1 = Archer("Mohan", 85)
hyd1 = HybridSoldier()

wizard1.attack()
archer1.attack()
hyd1.attack()
# notice that these two instances are executing the child class method and not the parent class method.

'''
This is polymorphism.
Even though we are using the same function, it is giving different output based on the object.
'''
