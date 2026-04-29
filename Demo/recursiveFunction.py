#Sum of natural numbers using resursive
def sum(n):

    if  n==1:  #base condition
        return 1
    else:   #recursive call
        return n + sum(n - 1)
    
n = int(input("Enter a number"))
print("Sum of numbers from 1 to",n,"is",sum(n))

#Factorial of a number using resursion
def fact(n):
    #Base Condition
    if n==0:
        return 1
    #Recursive Call
    else:
        return n*fact(n-1)
print ("Factorial of 5:",fact(5))
