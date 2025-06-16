
'''
ASSIGNMENT 4:
Module 5: Files, Exceptions, and Errors in Python

Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.


Expected Output:
 For example, if the user enters 25, the output should be:

'''

# Step 1: Take user input and write it to a file
user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data successfully written to output.txt.")

# Step 2: Append additional data to the same file
additional_input = input("\nEnter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

print("Data successfully appended.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
