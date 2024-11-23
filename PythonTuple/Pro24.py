"""
Author Shivam Rawat
Developer Python 
"""
#Tuple
# 1.Tuple are ordered collections of data item
# 2.Tuple can store multiple value of different datatype in one variable.
# 3.Tuple items are sepertaed by comma and enclosed within round bracket.
# 4.Tuple are immutable we cant alter tuple after creation.


# tup =(1) #one value in tuple will considered as int so ==>write like this for 1 value tup "tup =(1,)"
# print(tup)
# print(type(tup))

tup=(1,2,3,4,"Shivam")
print(tup)
print(type(tup))


# Tuple is not alterable.We cant modify tuple
# tup[0]=90   #will give error

# index wise print
print("Value at index ",0,"is :",tup[0])
print("Value at index ",1,"is :",tup[1])
print("Value at index ",2,"is :",tup[2])
print("Value at index ",3,"is :",tup[3])
print("Value at index ",3,"is :",tup[4])


## Negative indexing
print(tup[-3])   ## tup[len(tup)-3] ==tup[-3] 




if "Harry" in tup:
    print("Yes")
else:
    print("No") 


# Slicing in tuple :Tuple[Strt:end:jumpIndex] hence it return new tuple after slicing 
tup2=tup[1:3]
print(tup2)




















































