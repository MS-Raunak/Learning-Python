tea_shop = {
    "chai" : {"Masala" : "Testy", "Ginger" : "Zesty", "Green" : "Fresh"},
    "stationary" : {"Write" : "Pen", "Read" : "Book"}
} 


# print(tea_shop) # printing tea_shop
#print(tea_shop["chai"]) #printing all chai

# Retriving all elements from dictionary chai_shop
for items in tea_shop:
    for ele in tea_shop[items]:
        print(tea_shop[items][ele])


