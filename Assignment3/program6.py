# Write a Python program to read a file line by line and store it into a list

lines = []

file_path = 'C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt'  

try:
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
except FileNotFoundError:
    print("File not found.")

print("Lines from file stored in list:")
print(lines)
