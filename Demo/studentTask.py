file = open('Students.xlsx', 'w')
file.write("Name, ID")
file.write("Karma, 001")
file.write("Sangay, 002")
file.write("Namgyel, 003")
file.write("Tashi, 004")
file.write("Kinga, 005")
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