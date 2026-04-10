for i in range(1,4):# outer loop iterates  from 1 to 3
    for j in range(i):
        print(f"Outer loop iteration {i},inner loop iteration {j+1}")


for i in range (4):# it reperesents the number of rows of stars to be printed. it iterates from 0 to 3, which means it will print 4 rows of stars.
    for j in range(i):# it represents the number of stars to be printed in each row. 
        print("*",end="")# End parameter is used to specify what to print at the end of the output. By default, it is a newline character but here we are using space to print stars in the same line.
    print()#print a new line after each row of stars is printed.


#students Activity
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()#print a new line after each row of stars is printed.

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()