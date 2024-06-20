class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def print_name(self):
        print(f"My name is {self.first_name}, {self.last_name}, {self.age}")
class Student(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

myStudent= Student('John', 'Will',24)
myStudent.print_name()
myStudent2= Student('Belinda', 'Kim',34)
myStudent2.print_name()
myStudent3= Student('Greg', 'James', 31)