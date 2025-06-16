'''
ASSIGNMENT 5:
Module 6: Data Structures and Strings in Python

Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.


Expected Output:
Enter the student's name: Alice
Alice's marks: 85

Enter the student's name: Jhon
Student not found.
'''
# Step 1: Create a dictionary with student names and their marks
student_marks = {
    "Alice": 85,
    'Mandava':95,
    'Srinu':90,
    'Vasu':75,
    'Ramesh':80,
    'Suresh':68
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 and 4: Retrieve and display the corresponding marks or show a message if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")
