# Diff btw 'is' vs '=='
# The main difference between the is and == operators in Python is that is checks if two variables point to the same object in memory, while == checks if the values of two objects are equal


a=4
b="4"

print(a is b) # excalt location of object.
print(a == b) # value

c=[1,2,43]
d=[1,2,43]

print(c is d) # excalt location of object.
print(c == d) # value


e =3
f =3

print(e is f) # excalt location of object.
print(e == f) # value
 

g=(1,2)
h=(1,2)
print(g is h) # excalt location of object.
print(g == h) # value
 










