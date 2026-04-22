class Student:
    """
    A simple Student class demonstrating constructors in Python.
    """

    def __init__(self, name: str, marks: int):
        """
        Parameterized constructor to initialize student data.
        """
        self.name = name
        self.marks = marks

    def display(self):
        """
        Display student details.
        """
        print(f"Name: {self.name}, Marks: {self.marks}")


# Example usage
if __name__ == "__main__":
    s1 = Student("Priyanshu", 85)
    s1.display()

    s2 = Student("Abhishek", 86)
    s2.display()

        

        

    
