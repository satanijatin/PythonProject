# Can one block of except statements handle multiple exception?

try:
  
    result = 10 / 0
except (ZeroDivisionError, ValueError, TypeError):
  
    print("An error occurred")
