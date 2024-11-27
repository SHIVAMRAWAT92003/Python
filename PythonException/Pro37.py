# The 'finally' block is always executed, regardless of whether an exception occurred or not. It is typically used for cleanup tasks and releasing resources that need to be performed no matter what(ie when we have to close the file or we have to revoke the connection fronm db)


def func1():
  try:
      l=[2,3,4,5]
      i =int(input("Enter the input index: "))
      print(l[i])
  except:    
      print("Some error ocuured...")
  finally:
      print("This is finally block always executed.")    
 
 
func1() 