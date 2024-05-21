chai_types = {"Masala" : "Testy", "Ginger" : "Zesty", "Green" : "Fresh"}

#print key,value
for key,value in chai_types.items():
    print(key, value)

#Add new pair
chai_types["Earl Grey"] = "Citrus"
#print key,value
for key,value in chai_types.items():
    print(key, value)