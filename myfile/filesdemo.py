# f = open('C:/Users/JATIN/Documents/GitHub/PythonProject/myfile/mydemo.txt','w')
# f.write("Hello python")
# f.truncate(7)
# f.close()

# with open("C:/Users/JATIN/Documents/GitHub/PythonProject/myfile/mydemo.txt") as f :
#     text = f.readline()

#     while text:
#         print(text.strip())
#         text = f.readline()

with open('filename.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip()) 
        line = file.readline()
    

