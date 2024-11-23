"""
Author Shivam Rawat
Developer Python 
"""
#If-Else()



cash =int(input("Enter the budget you have...\n"))
if(cash>12000):
    print("Let Go Mall")
else:
    if(cash>5000 and cash<=12000 ):
        print("Book Resturant")
    elif(cash>1000 and cash<=5000):
        print("Lets go Cafe")
    else:
        print("Let go Street Shop")           
