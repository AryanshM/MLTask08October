class A:
    name="Aryansh Mishra, Class A"
    def fa(self):
        print("a function of class A has been called")
    def add(self, a, b):
        num1=a
        num2=b
        print(num1+num2)
class B(A):
   
    def sub(self, a, b):
        print(a-b)
    def fb(self):
        print("a function of class B has been called")
        print("class B inherits from class A ")
        
class C(B):
    
    def fc(self):
        print("a function of class C has been called")
        print("class C inherits from class B ")
        
class D(B):
    
    def fd(self):
        print("a function of class D has been called")
        print("class D inherits from class B ")
class E(C,D):
    def __init__(self, a, b):
        self.e1=a
        self.e2=b
    def fe(self):
        print(f"a={self.e1} b={self.e2}")
        print("a function of class E has been called")
        print("class E inherits from class C and D ")

e1=E(1,2)
e1.fe()
e1.fd()
e1.fc()
e1.fb()
e1.fa()
print(e1.name)
print(e1.add(2,5))