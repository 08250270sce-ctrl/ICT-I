no_of_Students = int(input("Enter the number of students: "))
i=1#initialization
student_names={}#empty dictionary to store the names of the students.
while i<=no_of_Students:#condition
    name=input("Enter the name of the student:")
    print("The name of the student{} is {}".format(i,name))
    i+=1#incremanting the value of i by 1 in each iteration of loop.
    student_names[i]=name#it adds the name of the students to the dictionary with the key as the value of i.

print(student_names)#it prints the dictionary containing the names of the students entered by the user.

#Inifinite loop
while True:
    print("This is an infinite loop. Press Ctrl+C to stop it.")




