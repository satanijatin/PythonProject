# Write a Python program to copy the contents of a file to another file.

try:
   
    source_file_path = input("Enter the path of the source file: ")
    destination_file_path = input("Enter the path of the destination file: ")
    
    with open(source_file_path, 'r') as source_file:
        
        file_content = source_file.read()
        
        
        with open(destination_file_path, 'w') as destination_file:
            
            destination_file.write(file_content)
    
    print("File copied successfully!")
    
except FileNotFoundError:
    print("One of the files does not exist.")
except Exception as e:
    print("An error occurred:", e)
