#function decaratue
'''
def add_chocolate (func):
    def wrapper():
        
        print("1")
        func()
        print("2")
        
    return wrapper
def a (func):
    def w():
        print("3")
        print("4")
        func()

def b (func):
    def w():
        print("3")
        print("4")
        func()
        
    return w
@add_chocolate
@a
@b
def ice_cream():
    print("main fun")
ice_cream()


@add_chocolate
@a
def ice():
    print("main fun2")
ice()
'''
#genaratur 
def add():
    yield "sai"
    yield 
    yield "koti"
    
a=add()
print(next (a))
print(next (a))
print(next (a))


