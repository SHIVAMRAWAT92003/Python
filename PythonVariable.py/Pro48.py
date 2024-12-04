x =4
def hello():
    x=5
    print(f"The local x is {x}")
    
print(f"The global x is {x}")  
hello()
x=6
print(f"The global x is {x}")  



z=10
def my_fun():
    global z
    z=6
    
my_fun()
print(f"The global z is {z}")  




