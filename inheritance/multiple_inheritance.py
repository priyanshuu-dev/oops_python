# multiple_inheritance.py

class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skills(self):
        print("Child: Coding")

c = Child()
c.skills()

# To call specific parent:
Father.skills(c)
Mother.skills(c)