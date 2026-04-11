"""
File: employee_class_input_output.py
Description: Example of a class using instance methods and user input.
"""

class Employee:
    
    def put_data(self):
        """Takes input from user and stores in instance variables"""
        self.id = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.marks = int(input("Enter Marks: "))
    
    def display(self):
        """Displays employee details"""
        print("\nEmployee Details:")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Marks:", self.marks)


# Creating object and calling methods
e = Employee()
e.put_data()
e.display()