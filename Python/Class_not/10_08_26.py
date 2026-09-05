'''
s={1,"hi",True,4.0}
print=(s)

s={1,2,3,4,5}
s1={1,2,3,4,5,6}
print(s1|s)
'''
a=int(input("Enter a value"))#1
b=int(input("Enter b value"))#2
def y(a,b):
    return(a+b)
x=y(a,b)
print(x)
'''
def x(a=2,b=5,c=0):
    print(a+b)
    print(a+b+c)
x(a=1)

def add(*a):
    print(a[0]+a[1])
    print(a[0]-a[1])
    print(a[0],a[1],a[2])
add(1,2,3)


def rec(n):
    if n==0:
     return
    else:
        print(n)
        rec(n-1)
rec(5)

n=[1,2,3]
def a(x):
    x.append(4)
    print(x)#call by referance

a(n)
print(n)# call by value

'''



















    
