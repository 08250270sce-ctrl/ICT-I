# Initialize data structures for books and authors
students_list = []# Initialize an empty list to store student names
students_dict = {}# Initialize an empty dictionary to store student details

# Function to add a student to the list and dictionary
students_list.append("Karma Sangay Namgyel")
students_dict["Karma Sangay Namgyel"] = {"age": "21", "grade": "A"}

students_list.append("Arjun Bhattarai")
students_dict["Arjun Bhattarai"] = {"age": "20", "grade": "B"}

students_list.append("Pralad Adhikari")
students_dict["Pralad Adhikari"] = {"age": "22", "grade": "A"}

students_list.append("Sangay Dorji")
students_dict["Sangay Dorji"] = {"age": "23", "grade": "B"}

# Searching for a student in the list and dictionary
search_name = input("Enter the name of the student to search: ")
if search_name in students_list:
    print(f"Student found! Details: {students_dict[search_name]}")#Output: Student found! Details: {'age': '21', 'grade': 'A'}
else:
    print("Student not found.")# Output: Student not found.

# Remove a student from the list and dictionary
remove_name = input("Enter the name of the student to remove or else enter to skip: ")# Output: Enter the name of the student to remove or else enter to skip: Arjun Bhattarai
if remove_name in students_list:
    students_list.remove(remove_name)
    del students_dict[remove_name]# Remove the student from the dictionary
    
    if remove_name not in students_dict.keys():  # Check if the student has any other details in the dictionary
        name_set.remove(remove_name)# Remove the student from the set if they have no other details in the dictionary



    print("Student removed successfully.")
    print("Students available along with their details:", students_dict)
    print("Just available students:", students_list)

else:
    print("Student not found.")