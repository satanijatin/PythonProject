# Write a Python program to count the number of lines in a text file.

file_path = 'C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt'

try:
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    print("Number of lines in the file:", line_count)
except FileNotFoundError:
    print("File not found.")
