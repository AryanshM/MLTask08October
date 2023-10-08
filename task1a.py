class Complex:
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag
    def show(self):
        print(f"{self.real} + {self.imag}i")
    def setReal(self,real):
        self.real=real
    def setImag(self,imag):
        self.real=imag
    def getReal(self):
        return self.real
    def getImag(self):
        return self.imag
    def add(self, other):
        print(f"Sum:{self.real+other.real} + {self.imag+other.imag}i")
    def sub(self, other):
        print(f"Difference:{self.real-other.real} + {self.imag-other.imag}i")
    def prod(self,other):
        print(f"Product:{(self.real*other.real)+(-(self.imag*other.imag))} + {(self.real*other.imag)+((self.imag*other.real))}i")
    
#creating object
cn1=Complex(2,5)
cn2=Complex(3,7)
#displaying 
cn1.show()
cn2.show()
#displaying using getter
print(f"{cn1.getReal()} + {cn1.getImag()}i")
print(f"{cn2.getReal()} + {cn2.getImag()}i")
cn1.add(cn2)
#setting real part of c1
cn1.setReal(3)
cn1.add(cn2)
cn1.sub(cn2)
cn1.prod(cn2)
