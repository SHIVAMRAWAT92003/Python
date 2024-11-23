"""
Author Shivam Rawat
Developer Python 
"""
#Match Case()

num =int(input("Enter the number"))

match num:
    case 0:
        print("X is 0")
    case 1:
        print("X is 1")
    case 2:
        print("X is 2")
    case 3:
        print("X is 3")
    case 4:
        print("X is 4")
    case _ if(num>500):
        print("X is greater then 500")
        
    case _ if(num<500 and num>100):
        print("X is greater then 500 and less then 100")
        
    case _ :
        print("X is ",num)
        
