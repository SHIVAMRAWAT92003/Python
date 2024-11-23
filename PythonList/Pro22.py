"""
Author Shivam Rawat
Developer Python 
"""
#List
# 1.List are ordered collections of data item
# 2.List can store multiple value of different datatype in one variable.
# 3.List items are sepertaed by comma and enclosed within squ bracket.
# 4.List are mutable we can alter list after creation.


list1 = [3,5,6,"Harry",True,4,9,"Shivam","Rawat",8,"Ram"]
print(list1)
print(type(list1))
print("Value at index ",0,"is :",list1[0])
print("Value at index ",1,"is :",list1[1])
print("Value at index ",2,"is :",list1[2])
print("Value at index ",3,"is :",list1[3])


# Negative indexing
# list1[len(list1)-3] ==list[-3] 
print(list1[-3]) 


if "Harry" in list1:
    print("Yes")
else:
    print("No")    


print(list1)
print(list1[1:-1])

# print(list_name[1(slices sta   rt):7(slice end):2(jump by value)])
print(list1[1:7:2])


# List Comprehension == List compresion means creating the list from  other iterable like lists,tuples,dictionaries,set an even in array and string.

list2=[i for i in range(5)]
print(list2)

list3=[i*i for i in range(5)]
print(list3)

list4=[i*i for i in range(5) if i%2==0]
print(list4)




