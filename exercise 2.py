class Fruits:
    def __init__(self, type_of_fruit, color, flavour):
        self.type_of_fruit= type_of_fruit
        self.color= color
        self.flavour= flavour

    def display(self):
        print(f"I love {self.type_of_fruit}, it is {self.color} and it is {self.flavour}")


my_favourite_fruit= Fruits('mangoes', 'yellow', 'sweet')
my_favourite_fruit.display()
my_favourite_fruit2= Fruits('strawberry', 'red', 'fruity')
my_favourite_fruit2.display()
my_favourite_fruit3= Fruits('lemon', 'green', 'sour')
my_favourite_fruit3.display()
