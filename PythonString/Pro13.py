"""
Author Shivam Rawat
Developer Python 
"""
#Strings Methods in python...



print("String are immutable in python")
name = "ShivamRawat"
friendName = "!NiKiRawat!!"
otherFrnd="shivam rawat Nicks rawat"
otherFrnd2="shivamrawatnicksrawat"
print(len(name))
print(name.upper())
print(name.lower())
print(name.replace("Shivam","Golu"))
print("rstrip() removing the trailing char from string ==> ",friendName.rstrip("!"))
print("The split() method splits the given string at the specified instance and return the seperated strings as a list items.",otherFrnd.split(" "))
print(otherFrnd.capitalize())
print(otherFrnd.center(50))
print(otherFrnd.count("rawat"))
print(otherFrnd.startswith("shi"))
print(otherFrnd.endswith("wat"))
print(otherFrnd.endswith("am",0,6))
print(otherFrnd.find("rawat"))
print(otherFrnd.index("rawat"))
print(otherFrnd2.isalnum()) #a-z,A-Z,0-9
print(otherFrnd2.isalpha()) #a-z,A-Z
print(name.islower()) 
print(name.isupper()) 

printStr1="helloMyBillo"
printStr2="helloMyBillo\n"
print(printStr1.isprintable()) 
print(printStr2.isprintable()) 

str3 ="    "
str4=" y "
print(str3.isspace())
print(str4.isspace())

print(otherFrnd.swapcase())
print(otherFrnd.title())




if "iva" in "Shivam":
    print("Yes")
else:
    print("No")    






