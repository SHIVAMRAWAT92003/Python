# tuple method

# we cant change tuple directly we an crrate a new  list while copy existing tuple in it and make changes in new list and then convert it into new tuple.


# countries = ("India","Pak","China","Bhutan","Indonesia","Japan","England")
# # copy in list from tup
# temp=list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[2]="Australia"
# # copy in tup from list
# countries = tuple(temp)
# print(countries)



# concatinate tuple
# c1=(1,2,3,4)
# c2=(9,8,7,6)
# c3=c1+c2
# print(c3)



# count method
# tup1=(0,0,2,3,0,0,0,7,5,0,9,0)
# print(tup1.count(0))


# return the index of the given value
# tup1=(0,0,2,3,0,0,0,8,9,7,5,0,9,0)
# print(tup1.index(0))
# print(tup1.index(7))
# print(tup1.index(999)) # for wrong value give error

tup1=(0,1,2,3,2,3,1,3,2,3)
res= tup1.index(3,4,8)
print('index of 3 in tup1 is:',res)


























