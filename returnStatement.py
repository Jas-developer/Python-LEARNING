#function = a block of code which exceited only when it is called.

def hello(name):
    print("Hello!" + name)


hello("jASON")



#creating a function that will recieve a fullname
def fullName(first_name,last_name):
    full_name = f"Hello {first_name} {last_name}"
    return full_name

greetings = fullName("Jason","Evaristo")


print(greetings)