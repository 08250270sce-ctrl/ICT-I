def sum():
    a=5
    b=10
    print("The sum of a and b is:",a+b)

def product():
    a=5
    b=10
    print("The product of a and b is:",a*b)

sum()
product()


#Example using parameters
#sum
def sum_with_parameters(x,y):
    print("The sum of",x,"and",y,"is:",x+y)
sum_with_parameters(3,7)

#product
def product_with_parameters(x,y):
    print("The product of",x,"and",y,"is:",x*y)
product_with_parameters(3,7)

def sum_with_return(x,y):
    return x+y
print("The sum of 4 and 6 is:", sum_with_return(4,6))

def product_with_return(x,y):
    return x*y          
print("The product of 4 and 6 is:", product_with_return(4,6))