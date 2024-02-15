# How Do You Handle Exceptions With Try/Except/Finally In Python? 
# Explain with coding snippets

try:
   
    x = 10 / 0 
except ZeroDivisionError:
    
    print("Division by zero is not allowed.")
finally:
  
    print("Finally block executed.")
