# Write a Python program to read a file line by line store it into a variable


file_path = 'C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt'

try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
except FileNotFoundError:
    print("File not found.")

print("File contents stored in variable:")
print(file_contents)
