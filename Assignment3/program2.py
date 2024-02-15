def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Example usage:
file_path = 'C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt'
contents = read_text_file(file_path)
if contents is not None:
    print("File contents:")
    print(contents)
