# Responding to the unwanted or unexpected events when a computer program runs.
# Exception handling deals with  these events to avoid program or system crashing and without this process, exception would disrupt the normal operation of a program.

# Prog1
# a = input("Enter the number:")
# print(f"Multiplication table of {a} ids: ")
# try:
#   for i in range (1,11):
#       print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)
    
# print("End of program:")          
    

# Prog2
# num = input("Enter the numerator: ")
# deno = input("Enter the denominator: ")

# print(f"Divison of {num} by {deno} is :")
# try:
#     div = int(num)/int (deno)
#     print(div) 
# except:
#     print("Something went wrong pls check value...")

# print("Thakyou")    










# Prog3
try:
    num= int(input("Enter the number:"))
    a = [6,7,8]
    print(a[num])
except ValueError:
    print("Number entererd is not an integer.")  
except IndexError:
    print("Out of index.")
    
    













































