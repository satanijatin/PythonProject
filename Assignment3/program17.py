# When is the finally block executed?

try:
   
    f = open('C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt', "r")
    result = 10 / 2
except ZeroDivisionError:
    
    print("Division by zero error occurred")
else:
    
    print("No exception occurred. Result is:", result)
finally:
    
    print("Closing the file")
    f.close() 
