
def word_count(s):
    # Your code here

    # Step 1: Check for special chars, remove
    # Step 2: Convert the entire string to lowercase
    # Step 3: Count each word, return count of each word
    # str.split()
    # if char is in:
    # ignored_chars = {": '  ,  . - + = / \ | [] {} () * ^ &}
    # for each letter in array
    # if letter is in dict of ignored chars
    # remove that from the array
    ignored_chars = {'"': None, ':': None, ';': None, ',': None, '.': None, '-': None, '+': None, '=': None, '/': None,
                     '\\': None, '|': None, '[': None, ']': None, '{': None, '}': None, '(': None, ')': None, '*': None, '^': None, '&': None, '': None }
    counts = {}

    for char in s:
        if char in ignored_chars:
            # print(char)
            s = s.replace(char, '')
    print('s print statement', s)
    words = s.lower().split()
    
    for word in words:
        if word in counts:
            print(word, counts[word])
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    
    
        
    
            
    

 
    
    # else:
    #     return {}


   
    
    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))