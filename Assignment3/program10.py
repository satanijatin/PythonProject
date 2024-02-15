# Write a Python program to count the frequency of words in a file.

from collections import Counter
try:
    with open('C:/Users/JATIN/Documents/GitHub/PythonProject/Assignment3/example.txt', 'r') as file:
        content = file.read()      
        words = content.split()
        word_freq = Counter(words)
        print("Word frequency in the file:")
        for word, freq in word_freq.items():
            print(f"{word}: {freq}")
except FileNotFoundError:
    print("File not found.")
