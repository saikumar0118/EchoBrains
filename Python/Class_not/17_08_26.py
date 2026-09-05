'''
f=open("One.txt","r")
b=f.read()
print(b)
f.close()
'''
'''#why we are using "with" keyword becose the we
dont needto close the operation and open operaton again and again'''
with open(r"D:\EchoBrains\Python\One.txt","r") as f:
    v=f.read()
    print(v)