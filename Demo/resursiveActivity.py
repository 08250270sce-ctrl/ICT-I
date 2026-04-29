def fun1(x, y):
    if x == 0:
        return y
    else:
        return fun1(x - 1, y + x)
    
x=int(input("Enter the number of x:"))
y=int(input("Enter the number of y:"))

print("The result for x and y is:",fun1(x,y))