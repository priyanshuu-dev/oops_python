class Student:
    """
    A class to calculate average marks of a student.
    """

    def __init__(self, name: str, phy: int, chem: int, maths: int):
        """
        Initialize student with marks in three subjects.
        """
        self.name = name
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def calculate_average(self):
        """
        Calculate and return average marks.
        """
        return (self.phy + self.chem + self.maths) / 3

    def display(self):
        """
        Display student details and average marks.
        """
        avg = self.calculate_average()
        print(f"Name: {self.name}")
        print(f"Average Marks: {avg:.2f}")


# Example usage
if __name__ == "__main__":
    name = input("Enter name: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))

    s1 = Student(name, phy, chem, maths)
    s1.display()
