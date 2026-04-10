# Initialize data structures
students_list = []
student_age = set()
student_grade = set()
students_dict = {}

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

students_dict["Karma Sangay Namgyel"] = {"age": 21, "grade": "A"}
students_dict["Arjun Bhattarai"] = {"age": 20, "grade": "B"}
students_dict["Pralad Adhikari"] = {"age": 22, "grade": "A"}
students_dict["Sangay Dorji"] = {"age": 23, "grade": "B"}

# Add student
add_student = input("Enter student name to add (or press Enter to skip): ")

if add_student:
    add_age = int(input("Enter age: "))
    add_grade = input("Enter grade: ")

    students_list.append(add_student)
    student_age.add(add_age)
    student_grade.add(add_grade)
    students_dict[add_student] = {"age": add_age, "grade": add_grade}

    print(f"Student '{add_student}' added successfully!")
else:
    print("No student added")

print()

# Search student
search_name = input("Enter student name to search: ")

if search_name in students_dict:
    print(f"Found: {search_name}, Age: {students_dict[search_name]['age']}, Grade: {students_dict[search_name]['grade']}")
else:
    print("Student not found")

print()

# Remove student
remove_student = input("Enter student name to remove (or press Enter to skip): ")

if remove_student in students_dict:
    students_list.remove(remove_student)
    del students_dict[remove_student]

    print("Student removed successfully!")
    print("Remaining students:", students_list)
    print("Details:", students_dict)
else:
    print("Student not found")