'''class sai():
    #methods
    #creatie object to access classs
  def fun(seif):
    print("hello")
a=sai()
a.fun()

class A():
    pass
a=A()

class clac():
    def add(self,a,b):# "self" is keyword to tell calss i am the indipende
        print("AddditionP:",a+b)
    def sub(self,a,b):
        print("Substaction:",a-b)
n=clac()
n.add(1,2)
n.sub(1,2)
'''
class student():
    def __init__(self,name,reg):# "self" is keyword to tell calss i am the indipende
      self.name=name
      self.reg=reg
    def dis(self):
       print(self.name,self.reg)

       
n=student("sai",1234)
n.dis()

