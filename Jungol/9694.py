class Person:
    def __init__(self, name, age):
       self.name = name 
       self.age = age
    def print(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

name, age = input().split()
#print(name, age)
p1 = Person(name, age)
p1.print()       


#2------------------------------------------------
class My_name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name, age = input().split()
person = My_name(name, age)

print(f"My name is {person.name}.")
print(f"I am {person.age} years old.")