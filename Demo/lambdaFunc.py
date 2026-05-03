name=input("Enter your name:")
greet=lambda x:print("Hello",x)
greet(name)

even_Odd=lambda x:"Even" if x%2==0 else "Odd"
num=int(input("Enter your number: "))
print(even_Odd(num))

#return multiple result
arith=lambda x,y: (x+y,x-y,x*y,x/y)
num1=int(input("Enter first number: "))
num2=int(input("Enter the second number: "))
print(arith(num1,num2))

#filter() select elements from a list that satisfy  a given comdition
mylist=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0, mylist)
print(list(even))

#Map Function():applies a lambda expression to each element and returns a map object.
mylist=[1,2,3,4]
double=map(lambda x:x*2,mylist)
#print(list(double))

mynewlist=(list(double))
print(mynewlist)
half=map(lambda x:x/2,mynewlist)
print(list(half))

#reduce(): This function repeatedly applies a lambda expression to elements of a list to combine them into single result.
from functools import reduce
mylist=[1,2,3,4]
mul = reduce(lambda x,y:x*y,mylist)
print(mul)

# student Activity: lambda to classify a number
number = lambda x: "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
user_input = int(input("Enter a number to classify: "))
print(number(user_input))