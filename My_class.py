#Create a Python class named Person.
class Person:
#The Person class should have the following attributes:
#name: representing the person's name.
#age: representing the person's age.
#gender: representing the person's gender.
    def __init__(self,name,age,gender):
        self.name= name
        self.age= age
        self.gender= gender
#Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
    def introduce(self):
        print('Hi my name is',self.name,'I am',self.age,'years old and I am a',self.gender)
#Create an instance of the Person class and call the introduce method to display the person's information.
result=Person('Gloria',24,'female')
result.introduce()
