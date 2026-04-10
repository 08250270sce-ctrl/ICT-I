# Initialize data structures
students_list = []# List to store student names
student_age = set()# Set to store unique ages of students
student_grade = set()# Set to store unique grades of students
students_dict = {}# Dictionary to store student details (name as key, age and grade as values)

# Add initial students (same style as yours)
students_list.append("Karma Sangay Namgyel")
students_list.append("Arjun Bhattarai")
students_list.append("Pralad Adhikari")
students_list.append("Sangay Dorji")

student_age.add(21)
student_age.add(20)
student_age.add(22)
student_age.add(23)

student_grade.add('A')
student_grade.add('B')

students_dict["Karma Sangay Namgyel"] = {"age": 21, "grade": "A"}# Adding student details to the dictionary with name as key and age and grade as values
students_dict["Arjun Bhattarai"] = {"age": 20, "grade": "B"}# Adding student details to the dictionary with name as key and age and grade as values
students_dict["Pralad Adhikari"] = {"age": 22, "grade": "A"}# Adding student details to the dictionary with name as key and age and grade as values
students_dict["Sangay Dorji"] = {"age": 23, "grade": "B"}# Adding student details to the dictionary with name as key and age and grade as values

# Add student
add_student = input("Enter student name to add (or press Enter to skip): ")# Prompt the user to enter a student name to add, or press Enter to skip adding a student

if add_student:
    add_age = int(input("Enter age: "))# Prompt the user to enter the age of the student being added, and convert the input to an integer
    add_grade = input("Enter grade: ")# Prompt the user to enter the grade of the student being added

    students_list.append(add_student)# Add the new student name to the students_list
    student_age.add(add_age)# Add the new student's age to the student_age set (ensuring uniqueness)
    student_grade.add(add_grade)# Add the new student's grade to the student_grade set (ensuring uniqueness)
    students_dict[add_student] = {"age": add_age, "grade": add_grade}#  

    print(f"Student '{add_student}' added successfully!")#  Print a success message indicating that the student has been added
    print("Current students:", students_list)# Print the current list of student names  
else:
    print("No student added")# Print a message indicating that no student was added

print()# Print a newline for better readability

# Search student
search_name = input("Enter student name to search: ")# Prompt the user to enter a student name to search for in the students_dict

if search_name in students_dict:
    print(f"Found: {search_name}, Age: {students_dict[search_name]['age']}, Grade: {students_dict[search_name]['grade']}")# If the student name is found in the students_dict, print the student's name, age, and grade using the dictionary values
else:
    print("Student not found")# If the student name is not found in the students_dict, print a message indicating that the student was not found

print()

# Remove student
remove_student = input("Enter student name to remove (or press Enter to skip): ")# Prompt the user to enter a student name to remove, or press Enter to skip removing a student

if remove_student in students_dict:
    students_list.remove(remove_student)# Remove the student name from the students_list using the remove() method
    del students_dict[remove_student]#

    print("Student removed successfully!")# Print a success message indicating that the student has been removed
    print("Remaining students:", students_list)#
    print("Details:", students_dict)#
else:
    print("Student not found")# Print a message indicating that the student was not found for removal