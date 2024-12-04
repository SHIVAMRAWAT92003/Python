# MAP = take seq of element as an input and return a seq of elements as an output.These func()can takes the func() as an argument.
# map(function,iterable)


l =[1,2,4,6,4,3]

#Way1
# def cube(x):
#     return x*x*x

# newl1=[]
# for item in l:
#     newl1.append(cube(item))
# print(newl1)  


#Way2  ===>MAP
# newl2 = list(map(cube,l))  
# print(newl2)  


#Way3  ===>Map with lambda
# newl3 = list(map(lambda x:x*x*x,l))  
# print(newl3)  



# Filter === filter function filters a seq of elements based on a given predicate(a fuction that return a boolean value ) and return a new seq containg only the elements that meet the predicate .
# filter(predicate,iterable)


# def filter_fun(li):
#     return li>2

# newl4=list(filter(filter_fun,l))
# print(newl4)


#REDUCE === the function argument is a function that takes in two argument and return a single value.The iterable argument is a sequence of element,such as a list or tuple. 
# The reduce function applies the function to the first two element in the iterable and then applies to the function to the result and the next elements,and so on.The reduce fun return the final result.

# from functools import reduce
# reduce(fun,iterable)

from functools import reduce
def mySum(x,y):
    return x+y
    
sum=reduce(mySum,l)
print(sum)

sum2=reduce(lambda x,y:x+y,l)
print(sum2)













































  