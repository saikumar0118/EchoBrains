#OPERATORs
a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
c=int(input("Enter C value:"))
#this inputs for 
x=int(input("Enter X value :"))
y=int(input("Enter Y value :"))
z=int(input("Enter Z value :"))


#Arathmetic Operators
print(" ")
print("#Arathmetic Operators for: ",a,b)
print("Addition:",a+b)              #used to add the values
print("Subtraction :",a-b)           #used to Subtrac the values
print("Multipication :",a*b)         #used to multiplay the values 
print("Divison in Flote :",a/b)      #used to Divison the value and the valuves in the "Flote type"
print("Flore Divison in int :",a//b) #this also do same process but the values in the "Intiger"
print("Remainder :",a%b)             # used to find the modules/remainder values
print("Exponentiation :",a**c)        #used to fine the power values

#Comparison Operator
print(" ")
print("Comparison Operators for: ",a,b)
print("A is Equval B True or False :",a==b)
print("A is Not Equval B True or False :",a!=b)
print("A is Greater than B True or False :",a>b)
print("A is Less than B True or false :",a<b)
print("A is Greater than Equval to B True or False :",a>=b)
print("A is Less than Equval to B True or False :",a<=b)


#Logical Operator
print(" ")
print("Logical Operator for: ",x,y)
print("checking the X and Y equal or not,any one of False the statement will false: ",x==y and x!=y)
print("checking the X and Y equal or not,any one of True the statement will True: ",x==y or x!=y)
print("when the Condison is False Statement is True : ",not(x==y and x!=y))


#Bitwise Operators
'''
8 4 2 1 =Values
---------------
0 0 0 0 =0        
0 0 0 1 =1
0 0 1 0 =2
0 0 1 1 =3
0 1 0 0 =4
0 1 0 1 =5.....n
Qurtion: find the OR AND gate funtion for 2 and 3 number
SOl: 8 4 2 1=(OR)| 8 4 2 1=(AND) |Q:Right and Left shift for 3 in 2 times?
     --------    | -------       |RIGHT SHIFT      |LEFT SHIFT    |Q:It reverses every bit
     0 0 1 0 =2  | 0 0 1 0 =2    |8 4 2 1          |8 4 2 1       |ex: -5=5
     0 0 1 1 =3  | 0 0 1 1 =3    |----------       |----------    |     4=-4
     ----------  | ----------    |0 0 1 1 =3       |0 0 1 1| =3   |
     0 0 1 1 =3  | 0 0 1 0 =2    |0 0 0 0 =0       |1 1 0 0| =12  |

'''
print(" ")
print("Bitwise Operators for",x,y)
print("finding the X,Y individual bits of a number for AND(&): ",x & y)
print("finding the X,Y individual bits of a number for OR(|): ",x | y)
print("finding the X,Y individual bits of a number for XOR(^): ",x ^ y)
print("finding the X,Y individual bits of a number for NOT(~): ",~ y)
print("Shifting the bits numbers to the Left side (<<): ",x<<1)
print("Shifting the bits numbers to the right side (>>):",y>>1)


#Assigment operators
print(" ")
a+=10
b-=10
c*=10
x/=10
y%=10
z**=10
print("Assigment Operators for: ",x,y)
print("Addition Assignment (+=): ",a)
print("Subtraction Assigment (-=): ",b)
print("Multipication Assigment (*=): ",c)
print("Divison Assigment (/=): ",x)
print("Exponentiation assigment (**): ",z)