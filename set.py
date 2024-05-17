
#set in python 
utensils = {"fork","spoon","knife"} #this is a set 
dishes = {"bowl","plate","cup", "knife"}


#i would like to see what utensils have that dishes doesnt
#print(utensils.difference(dishes))

#I would like to see what they have in common 
common = utensils.intersection(dishes)
difference = utensils.difference(dishes)

print(f"What they have in common is :{common}")
print(f"Their difference is : {difference}")


#a set is a collection that is unordered and un indexed










