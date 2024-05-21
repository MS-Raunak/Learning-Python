myList1 = [1,2,3,4,5]
print(myList1)  # [1, 2, 3, 4, 5]
print(myList1[0]) # 1


myList2 = myList1;
print(myList2) #[1, 2, 3, 4, 5]

list = [4,3,2,1] 
list2 = list[:]
list[0] = 5;
print(list) # [5,3,2,1]
print(list2) # [4,3,2,1]


l=[3,4,5];
l2=l
l[0]=19
print(l) #[19, 4, 5]
print(l2)#[19, 4, 5]