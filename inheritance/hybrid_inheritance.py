# hybrid_inheritance.py

class A:
    def method_A(self):
        print("Class A")

class B(A):
    def method_B(self):
        print("Class B")

class C(A):
    def method_C(self):
        print("Class C")

class D(B, C):
    def method_D(self):
        print("Class D")

d = D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()