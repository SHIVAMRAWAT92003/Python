"""
Author Shivam Rawat
Developer Python 
"""

# TypeCasting in python...
print("Converting from one datatype to onother datatype is known as typecasting. ")
print("Typecasting are of 2 type:\n 1.Implicit:Conversion from one datatype to onother datatype done by interpreter automatically(low-->high) \n2.Explicit: plicit:Conversion from one datatype to onother datatype, done by programmer manually.")

# Implicit Typecasting
print("Implicit Typecasting Example:")
a =1
b=2.1
print("Before Conversion:Type of a is",type(a),"Type of b is",type(b))
a=a+b
print("After Conversion:Type of a is",type(a),"Type of b is",type(b))



print("Explicit Typecasting Example 2:")
a ="1"
b="2"
print("Before Conversion:Type of a is",type(a),"Type of b is",type(b),"a+b is :",a+b)
a=int(a) 
b=int(float(b))
print("After Conversion:Type of a is",type(a),"Type of b is",type(b),"a+b is :",a+b)







