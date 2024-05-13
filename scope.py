#learning the scope of a python code

#example of a local scope
def myfunc():
    x  = 300
    print(x)
    
myfunc()

#function inside the function 
def myInnerFunction():
    x = 300
    def myinnerfunc():
        print(f"The result of inner function is {x}")
    myinnerfunc()
    
myInnerFunction()