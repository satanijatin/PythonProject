# When will the else part of try-except-else be executed? 

try:
    # code that may raise exceptions
    result = 10 / 2
except ZeroDivisionError:
    # handle division by zero exception
    print("Division by zero error occurred")
else:
    # code to execute if no exception occurs
    print("No exception occurred. Result is:", result)
