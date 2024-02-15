# How many except statements can a try-except block have? Name Some 
# built-in exception classes
try:
    # code that may raise exceptions
    result = 10 / 0
except ZeroDivisionError:
   
    print("Division by zero error occurred")
except ValueError:
    print("Value error occurred")
except Exception as e:
    print("An unexpected error occurred:", e)

