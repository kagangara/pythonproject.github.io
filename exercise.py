class Cars :
    def __init__(self, Model, Year_of_Manufacture, Type, Color):
        self.Model=Model
        self.Year_of_Manufacture=Year_of_Manufacture
        self.Type=Type
        self.Color=Color
    def display(self):
        print("My dream car is" + self.Model + " manufactured in " + self.Year_of_Manufacture + " being a" +self.Type +" in color" + self.Color)


my_dream_car= Cars(' Mercedes', '1980', ' Brabus', ' matte grey')
my_dream_car.display()
my_dream_car2= Cars(' Ford', '2024', ' Raptor', ' black')
my_dream_car2.display()
my_dream_car3= Cars(' Cardillac Escalade', '1890', ' SUV', ' black')
my_dream_car3.display()
my_dream_car4= Cars(' Mercedes', '1960', ' G-Wagon', ' silver')
my_dream_car4.display()



