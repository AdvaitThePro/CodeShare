# Inheritence.py
#
# Made by Advait
# 
# Copyright Ralph(C) Inc.
#
# Made on 7/18/2020

class Person:   
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        output = f'Hello, {self.name}!'
        print(output)

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    
    def sing_school_song(self):
        output2 = f'Ode To {self.school}'
        print(output2)

    def say_hello(self):
        # Let the parent do some work
        super().say_hello()        
        # Here is some custom code
        print("Sup Boi. Never mess with the pros.\nAdvaitThePro")

    def __str__(self):
        return f"{self.name} attends {self.school}"

student = Student("Advait", "Yumin Primary School")
student.say_hello()
student.sing_school_song()
print(student)

# Inheritance
# What are you?
print(f"Is this a student? {isinstance(student, Student)}")
print(f"Is this a person? {isinstance(student, Person)}")
print(f"Is this student a person? {issubclass(Student, Person)}")
print("Does the persson have friends? True")