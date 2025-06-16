'''
ASSIGNMENT 4:
Module 5: Files, Exceptions, and Errors in Python

Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

Expected Output:

If the file exists:
Reading File content:

Line  1 :  This is a sample text file.
Line  2 :  It contains multiple lines.

If the file does not exist:
Error: The file 'sample.txt' was not found.
'''


# Method 1

filename = 'sample1.txt'

try:
    i = 1
    with open(filename, 'r') as file:
        print("Reading File content:\n")
        for line in file:
            print("Line ", i, ": ", line.strip())
            i += 1
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Method 2 using function
def read_file(filename):
    try:
        i=1
        with open(filename, 'r') as file:
            print("Reading File content:\n")
            for line in file:
                print("Line ",i,": ",line.strip())
                i+=1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function with 'sample.txt'
read_file('sample.txt')
