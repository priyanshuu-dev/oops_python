"""
File: student_class_basic.py
Description: Basic example of a class in Python using class attributes.
"""

class Student:
    # Class attributes (shared by all objects)
    name = "Priyanshu"
    roll = 1408


# Creating objects of Student class
s1 = Student()
print("Student 1 Name:", s1.name)

s2 = Student()
print("Student 2 Roll:", s2.roll)