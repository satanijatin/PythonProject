# Write a Python program to write a list to a file.

def write_list_to_file(lst, filename):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(str(item) + '\n')


my_list = [1, 2, 3, 4, 5]
write_list_to_file(my_list, 'C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example2.txt')
