file = open('Students.xlsx', 'w')
file.write("Name, ID\n")
file.write("Karma, 001\n")
file.write("Sangay, 002\n")
file.write("Namgyel, 003\n")
file.write("Tashi, 004\n")
file.write("Kinga, 005\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter a name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()