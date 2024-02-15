# Write a Python program to append text to a file and display the text. 


ddd=open('C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt','a')
ddd.write("program3 \n hi hello world")
ddd.close

ddd=open('C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt','r')
aa=ddd.read()
print(aa)
ddd.close
