"""
Author Shivam Rawat
Developer Python 
"""
#For Break and Continue

print("In Case of break it will move out of loop")


for i in range(20):
    if(i ==15):
       break
    print("5 X",i,"=",5*i)

print("In Case of continue it will skip that iteration and continue next iteration")
for i in range(20):
    if(i ==15):
       continue
    print("5 X",i,"=",5*i)

