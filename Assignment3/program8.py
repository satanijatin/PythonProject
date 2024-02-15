# Write a python program to find the longest words. 

text = "This is an example sentence to find the longest words in a given text."
words = text.split()
max_length = max(len(word) for word in words)

longest_words = [word for word in words if len(word) == max_length]

print("Longest word(s):")
for word in longest_words:
    print(word)
