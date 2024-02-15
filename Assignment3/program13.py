# Explain Exception handling? What is an Error in Python?

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
except Exception as e:
    print("An error occurred:", e)
else:
    print("No exceptions occurred.")
finally:
    print("Cleanup tasks can go here.")
