'''
class A():
    def a(self):
        print("hi")
class B(A):
    def b(self):
        print("hello")
class C(B):
    def c(self):
        print("welcome")
obj= C()

class A():
    def a(self):
        print("hi")
class B():
    def b(self):
        print("hello")
class C(A,B):
    def c(self):
        print("welcome")
obj= C()
'''

#methoed over riting 
class father():
    def age(self):
        print("i'm 50")
class son(father):
    def age(self):
        print("I'm 20")
obj=son()
obj.age()
