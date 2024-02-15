filename = 'C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt'
n = int(input("Enter line you want : "))
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[:n]:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
