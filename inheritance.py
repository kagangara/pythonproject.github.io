class Animals:
    def speak(self):
        print('Animal is speaking')
class Dog(Animals):
    def bark(self):
        print('Dog is barking')
class Cat(Animals):
    def meow(self):
        print('Cat is meowing')
class Cow(Animals):
    def moo(self):
        print('Cow is mooing')
d=Dog()
d.bark()
c=Cat()
c.meow()
d.speak()
C=Cow()
C.moo()