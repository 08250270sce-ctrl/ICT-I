# Initialize data structures for books and authors
students_list = []#  we have to initialized an empty list to store student names
student_age = set()#creating an empty set
student_grade = set()#creating an empty set
students_dict = {}# We have to initializd an empty dictionary to store student details

#  This are some of the function to add a student to the list and dictionary
students_list.append("Karma Sangay Namgyel")#adding student name to the list
students_list.append("Arjun Bhattarai")#adding student name to the list
students_list.append("Pralad Adhikari")#adding student name to the list
students_list.append("Sangay Dorji")#adding student name to the list
student_age.add(21)#adding student age to the set
student_age.add(20)#adding student age to the set
student_age.add(22)#adding student age to the set
student_age.add(23)#adding student age to the set
student_grade.add('A')#adding student grade to the set
student_grade.add('B')#adding student grade to the set
student_grade.add('A')#adding student grade to the set
student_grade.add('b')#adding student grade to the set
students_dict['Karma Sangay Namgyel'] = {'age': 21, 'grade': 'A'}#adding student details to the dictionary
students_dict['Arjun Bhattarai'] = {'age': 20, 'grade': 'B'}#adding student details to the dictionary
students_dict['Pralad Adhikari'] = {'age': 22, 'grade': 'A'}#adding student details to the dictionary
students_dict['Sangay Dorji'] = {'age': 23, 'grade': 'B'}#adding student details to the dictionary

add_student = input("Enter the student name to add or else enter to skip: ") #taking input for student name to be added to the existing list of students
add_age = int(input("Enter the age of the student: ")) #taking input for student age to be added to the existing set of student ages and also to be added to the dictionary along with the student name
add_grade = input("Enter the grade of the student: ") #taking input for student grade to be added to the existing set of student grades and also to be added to the dictionary along with the student name

if add_student: #checking if the input for student name
    students_list.append(add_student) #adding student name to the list
    student_age.add(add_age) #adding student age to the set
    student_grade.add(add_grade) #adding student grade to the set
    students_dict[add_student] = {'age': add_age, 'grade': add_grade} #adding student details to the dictionary 
    print(f"Student added successfully! The age of the student '{add_student}' is {students_dict[add_student]['age']} and the grade is {students_dict[add_student]['grade']}.")#printing the details of the new student added before
else:
    print("No student added")#printing the reminder if no student are added
print()#printing a blank line
search_name = input("Enter the student name to search: ")#taking input for student name to be searched in the existing list of students and also to be searched in the dictionary to get the details of the particular student if found
if search_name in students_list: #checking if the input for student name is there in the existing list of students
    print(f"Student found! The age of the student '{search_name}' is {students_dict[search_name]['age']} and the grade is {students_dict[search_name]['grade']}.") #printing the details of the student if found in the list and in the dictionary
else: #another condition to be executed if the first condition is not satisfied
    print("Student not found")#printing the reminder if the student is not found in the list and in the dictionary
print()#printing a blank line
remove_student = input("Enter the student name to remove or else enter to skip: ")#taking input for student name to be removed from the existing list of students and also to be removed from the dictionary along with the details of the particular student if found
if remove_student in students_list: #checking if the input for student name is there in the existing list of students or not
    remove_age = students_dict[remove_student] #getting the age of the student to be removed from the dictionary before removing the student from the list and from the dictionary
    remove_grade = students_dict[remove_student] #getting the grade of the student to be removed from the dictionary before removing the student from the list and from the dictionary
    students_list.remove(remove_student) #removing student name from the list
    del students_dict[remove_student] #removing student details from the dictionary

    print("Student removed successfully!") #printing the message of success if the student is removed successfully
    print("Students left along with their details: ", students_dict) #printing the details of the remaining students after removing the particular student from the dictionary
    print("List of students left: ", students_list) #printing the list of remaining students after removing the particular student from the list
else: #setting the second condition to be executed if the first condition is not satisfied
    print("Student not found") #printing the message of successfully excuting the second condition
print()#printing a blank line 