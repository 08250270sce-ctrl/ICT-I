name=input("Enter your name:")
for i in name:
    print(i)

#Iterating over list
li=["Python Programming","Python Fundamentals","Python Interview Question"]
for x in li:# x is the variable that takes the value of each element in the list li during each iteration of the loop
    print(x)

lenli=len(li)#lenli() returns the number of items in the list li i.e. 3. This value is stored in the variable lenli
for i in range(lenli):# i is the variable that takes the value of each index.
    print(li[i])

#tuple
new_tuple=tuple(li)#converting list to tuple
for i in new_tuple:
    print(i)

new_set=set(li)#converting list to set 
for i in new_set:
    print(i)
