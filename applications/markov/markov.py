import random

# Read in all the words in one go
following = {}
with open("input.txt") as f:
    words = f.read()
    words = words.split()
print(words)

# TODO: analyze which words can follow other words
# Your code here
for word in words:
    if words[word + 1] is not None:
        words[word] = words[word+1]



# TODO: construct 5 random sentences
# Your code here

