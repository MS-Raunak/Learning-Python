chai_types = {"Masala" : "Testy", "Ginger" : "Zesty", "Green" : "Fresh"}

# copy() :- used to copy items from one dictonary to another dictonary
# new_chai = chai_types.copy()
# print(new_chai["Masala"])

# pop(key) :- it is used to delete specified items from dictonary

# chai_types.pop("Green") 
# for chai in chai_types:
#     print(chai_types[chai])  #fresh is deleted

# popitems() :- It is used to delete last item from dictonary, it doesnot take argument
# chai_types.popitem()    
# for chai in chai_types:
#     print(chai_types[chai])


# get(key):- used to get value for specified key from dictionary
print(chai_types.get("Masala"))  

#clear() :- used to delete all items from dictionary
chai_types.clear()
print(chai_types)

