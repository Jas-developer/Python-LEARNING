#learning the scope of a python code

#example of a local scope
def myfunc():
    x  = 300
    print(x)
    
myfunc()

#function inside the function 
def myInnerFunction():
   global x 
   x = 301
def myinnerfunc():
        print(f"The result of inner function is {x}")
        myinnerfunc()
    
myInnerFunction()

turnGlobal = x
print(turnGlobal)
#now this is the global scope

global name
name = "Jason Evaristo"

testGlobal = f"Testingt the global variable which is {name}"
def display(param):
    print(param)
    
display(testGlobal)
