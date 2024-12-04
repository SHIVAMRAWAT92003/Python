# if __name__ == "__main__":Idiom is a common pattern used in python scripts to deteremine wheather the script is being drectly or being imported as a module into other script. 

def welcome():
    print("Hey your welcome my dear....")
   
print(__name__)
if __name__ == "__main__":
    welcome()