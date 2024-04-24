#PYTHON ARITHMETIC OPERATORS 
#addition 
add = 10 + 5
print(add) # result is 15
#substraction
substraction = 10 - 5
print(substraction) # result is 5
#multiplication 
multiplication = 10 * 5
print(multiplication) # result is 50
#division
division = 10 / 5
print(division) # result is 2 
#modulus
modulus = 10 % 5
print(modulus) # result is 0
#Exponentiation
exponentiaton = 10 ** 5
print(exponentiaton) # result is  
#floor division
flordiv = 10 // 5
print(flordiv) #result is  2

#python list
#list are customizable 


listSample = ["apple","banana","cheery"]
print(listSample)
#print banana
print(listSample[1])
#change banana to orange
listSample[1] = "orange"
print(listSample)
#print the length or the number amoount of the list
print(len(listSample));

# list with multiple types of different data types
multiTypes = [1,"Data", True, False, 2.0]
#printing the multi types
print(type(multiTypes))
print(type(multiTypes[4]))

#creating list constructor 
multiTypes = list(("apple","banana","orange"))
print(type(multiTypes))

#duplicates meaning they can have items with the same value
#tuple are declared with circle bracket 
data_collector = ("list","tuple","set","dictionary")
print(type(data_collector))
print(len(data_collector))
#tuple items can be of any data types
#when creating a construction for any collection data types
#you must enclosed them with rounded bracket

#accessing range of the list

list_range_names = ["Rojon","Dave","Dev","Ken","James"]
#printhing the name james
print(list_range_names[-1])
#printing the name Ken
print(list_range_names[-2])
#printing from rojon to ken
print(list_range_names[0:5]) #range of indexes

#check if the name do exist 

if "Dev6" in list_range_names:
    confirmation_string = "is here, Existing"
    print("Dev",confirmation_string)
else:
    print("No that mothefucker do not exist at all");
    
    
#list change a range of item values

this_list = ['Software Engineer', 'Accounting Staff', 'Data Scientist'];

if "Data Scientist" in this_list:
    this_list[-1] = "Data Engineer"
    
print(this_list)

this_list[:2] = ["Data Engineer","Data Analyst"]
print(this_list)

#the data engineer is double so we gonnna insert a new different data
this_list.insert(2,"Data Scientist")
#printing the new list

print(this_list);

this_list[-1] = "Web Developer"
#print the new 
print(this_list);
#add Devops Engineer
addNew = ["Devops Engineer","Network Engineer"]
this_list.extend(addNew) #extend will concatinate 2 arrays 
this_list.append("I.T Support")
print(this_list)

#declaring tupple then extend it to my list
moreJob = ("Human Resource", "Software Developer")
this_list.extend(moreJob)
print(this_list)

#remove 
this_list.remove(this_list[-3])
print(this_list)

this_list.pop(-2)
#printhing the list without HR
print(this_list)

del this_list[-2]
print(this_list)

check_length = len(this_list)
#printhing the list with the number of length 
print(check_length)    
#dictionaries are just like objects 

personInformation = {
  "names": ["Jason","John","Evaristo"],
  "cars": ["Ford","Honda","Civic"],
  "addresses": ["Posadas", "Devera", "Sara"],
  "Job": ["Software Engineer", "Data Engineer", "Data Scientist"]
};

#objects in python is called dictionary
print(personInformation["names"][0]);

#this concatination
jason = f"Hi my name is {personInformation['names'][0]} and my job is a {personInformation['Job'][0]}"
print(jason)

#if and else / else if in python 

a = 23
b = 24

#if and else 
if a > b:
    person_a = personInformation["names"][0]
    print(person_a)
elif b > a:
    print(personInformation["names"][1])
    
#while loop   
i = 1
while i <= 6:
    print(i)
    i += 1
    
#for loop
fruits = ["apple","banana","cherry"];

for x in fruits:
    print(x) #it will print all the contents of fruits list
    
#looping through a string
work = "softwareengineer"

for x in work:
    print(x)
    
    
for x in fruits:
    print(x)
    if x == "banana":
        break
    
for x in fruits:
    if x == "banana":
        break
    print(x)
    
    
#continue will basically skip the target index
for x in fruits:
    if x == "banana":
        continue
    print(x)