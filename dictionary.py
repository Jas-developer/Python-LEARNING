#learning dictionary
captitals  = { "USA": "Washington DC", "PH":"Manila", 'CHINA':"Bejing"}

#print the capital of USA
print(captitals.get("USA"))
#print the keys
print(captitals.keys())
#print the values
print(captitals.values())
#print everything
print(captitals.items())


for x, val in captitals.items():
    print(x, val)
    
    
    
for y,x in captitals.items():
    print(y)
    
    
    
captitals.update({'Germany':"Berlin"})


for x in captitals.items():
    print(x)