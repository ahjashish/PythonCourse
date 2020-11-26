# blueprint of objects
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  # Attribute or Property
        self.age = age
        print("I get printed at every instance created")

    def run(self):
        print(f"{self.name} is running")

    @classmethod  # we can use this method without instantiating the class
    def add_things(cls, n1, n2):
        return cls('Jojo', n1 + n2)

    @staticmethod  # same as @classmethod, only thing is we don't pass the class as argument, and hence can't use its attribute
    def add_things2(n1, n2):
        return n1 + n2


player1 = PlayerCharacter("Rohan", 22)
player2 = PlayerCharacter("Mohan", 98)
player2.attack = True  # creating a new attribute for the player2

print(player1)  # Memory location of the object
print(
    player1.name)  # Notice that we are accessing the attributes, and hence we are not using the curly brackets at the end
print(player1.age)

print(player2)
print(player2.name)
print(player2.age)

print(player1.run())  # Here we are accessing the method, and hence using curly brackets

print(player2.attack)

player1 = PlayerCharacter.add_things(4, 5)
print(player1.name)
print(player1.age)
print(player1.membership)

print(PlayerCharacter.add_things2(45, 5))
# print(player2.membership)     # gives error

'''
Note: Self refers to the object itself. So, self.name is nothing but player1.name
this way by using self, we pass the object itself to the class.
Every class method should have first argument as 'self'
and first method should be __init__ method.
'''
