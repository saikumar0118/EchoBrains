
def number():
    for i in range(1,11):
        yield i 
for num in number():
    print(num)

def number():
   for i in range(1,21):
     a=i%2==0
     yield i
for num in number():
    print(num)
    

def number():
    for i in range(1,11):
        a=i**2
        yield a
for num in number():
    print(num)