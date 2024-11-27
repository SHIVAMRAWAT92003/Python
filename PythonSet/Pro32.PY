"""
Author Shivam Rawat
Developer Python 
"""
# Set

s1 ={1,2,5,6,8,0}
s2={3,5,6,7,9}


# Union 
# print(s1.union(s2))

# update
# s1.update(s2)
# print(s1,s2)

# Intersection (jo common h dono mein )
# print(s1.intersection(s2))


# Intersection update
# s1.intersection_update(s2)
# print(s1)


# symmetric (jo common nahi h dono mein )
# print(s1.symmetric_difference(s2))


# diffeence ()
# print(s1.difference(s2))


# Disjoint Set = set which are completly differenrt from each other.
s3={"tok","mad","ber","del"}
s4={"tok","mad","ber","del"}
s5={"tok2","mad2","ber2","del2"}
s6={"tok","mad","ber","del","mub","abul"}

# print(s3.isdisjoint(s4))
# print(s3.isdisjoint(s5))



# superset
# print(s6.issuperset(s3))


# add() ==> if you want to add 1 item.
# s6.add("kashmir")


# update() ==> if you want to add more then 1 item.
# s6.update("Helia","Panisa","bukra")


# remove ==raise error when we try to remove non present element./ discard==not raise error when we try to discard non present element.
# s6.remove("tok")

# pop => remove last element from the set but catch is we dont known which element is removed as set are unordered.
# s6.pop()


# del ==>delete entire set using del keyword.
# del s6 
# print(s6)

# clear ==>we want to del all elements but not the set.
# s6.clear
# print(s6)

if "mad" in s6:
    print("Yes present")
else:
    print("Absent.")    
    








































