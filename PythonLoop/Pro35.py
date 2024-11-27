# Interview: can we use else with for/while loop ?
# yes


# Question 1
for i in range(5):
    print(i)
else:
    print("Sorry i over range...")    


# Question 2
for i in range(5):
    print(i)
    if i==4:
        break

else:
    print("Sorry i over range...")    
# Note : Else block will only run after the sucessfully completion of for loop.
# here because of break loop not completly fully so it will give error. 



# Question3 
i=0
while i<7:
 print(i)
 i=i+1
else:
    print("Sorry no i")  
    
    
    
# Questio4
i=0
while i<7:
 print(i)
 i=i+1
 if i==4:
  break
else:
    print("Sorry no i")  











