"""
Author Shivam Rawat
Developer Python 
"""
#For Function()


# Func 1
def name(fname="Shivam",mname="Singh",lname="Rawat"):
    print("Hello,",fname,mname,lname)

name()    
name(mname="Dhirendra")    
name(mname="Dhirendra",lname="Singh Rawat")


# Func 2
# fun_name(*para) ==>this takes values as a tuple.
def avg(*numbers): 
    sum=0
    for i in numbers:
        sum=sum+i
    print("Avg is",sum/len(numbers))    
       
avg(1,2)    
avg(1,2,4,5,6,7,8,8)    
avg(1,2,4,4,10)    
    
    
    
    
# Func 3
# fun_name(**para) ==>this takes values as a dict.
# name = {
#     "mname": "Dhirendra",
#     "lname": "Singh Rawat",
#     "fname": "Barren"
# }

def dicname(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

dicname(mname="Dhirendra", lname="Singh Rawat", fname="Barren")


# Func 4
def sumOfNatural(a):
    sum =0
    for i in range(a):
        sum=sum+i  #1 2 3 4
    return sum

res = sumOfNatural(5); 
print(res)   
        





























