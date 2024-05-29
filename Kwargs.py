def hello(**kwargs):
    full_name = f"Hello {kwargs["first"]} {kwargs["middle"]} {kwargs["last"]}, Have a great day!"
    print(full_name)    
    
    
    
    
hello(first="Jason",middle="Dude",last="Amante")



class Names:
    def __init__(self,first,middle,last):
        self.first_name = first
        self.middle_name = middle
        self.last_name = last
        
        
person_1 = Names("Jason","Amante","Evaristo")
person_1 = Names("Jason","Amante","Evaristo")
person_1 = Names("Jason","Amante","Evaristo")

list_1 = [person_1.first_name,person_1.middle_name,person_1.last_name]
list_2 = [person_1.first_name,person_1.middle_name,person_1.last_name]
list_3 = [person_1.first_name,person_1.middle_name,person_1.last_name]

persons = [list_1,list_2,list_3]
    
    

#learning kwargs 
def learn_kwargs(**names):
    for name in names.items():
        for n in name:
            print(n)
            
learn_kwargs(persons)