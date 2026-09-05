'''
class A():
    def __init__(self):
        print("Hello")
class B(A):
    def __init__(self):
        super() .__init__()
        print("How are u")
class C(B):
    def __init__(self):
        super() .__init__()
        print("i am fine")        
obj=C()
'''

#class2
class A():
    def __init__(self,name1):
        self.Name1=name1
    def X(self):
        print("name:",self.Name1)
class B(A):
    def __init__(self,name1,name2,):
        super() .__init__(name1)
        self.Name2=name2
    def Y(self):
        print("name:",self.Name2)
class C(B):
    def __init__(self,name1,name2,name3):
        super() .__init__(name1,name2)
        self.Name3=name3
    def Z(self):
        print("name:",self.Name3)
class D(C):
    def a(self):
    print("thanks")
obj=C("sai","lav","koti")
obj.X()
obj.Y()
obj.Z()
'''
# Task 2
class fruit():
    def __init__(self,color):
        self.colour=color
        print(self.colour)
apple=fruit("Blue")

# task 3
class teacher():
    def __init__(self,name,reg):
        self.Name=name
        self.RegNo=reg
    def display(self):
        print(self.Name,self.RegNo)
t1=teacher("sai",1)
t2=teacher("lav",2)
t1.display()
t2.display()

#task4
class calculator():
    def __init__(self,a,b):
        self.A=a
        self.B=b
    def add(self):
        print("add",self.A + self.B)
    def sub(self):
        print("sub",self.A - self.B) 
    def mul(self):
        print("mul",self.A * self.B)
    def div(self):
        print("div",self.A / self.B)
A=calculator(2,2)
A.add()
A.sub()
A.mul()
A.div()
'''

    
