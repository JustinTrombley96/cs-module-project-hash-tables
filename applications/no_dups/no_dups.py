def no_dups(s):
    # Your code here
    words = {}
    result = ''
    string = s.split()
    for word in string:
        # print(string)
        if word not in words:
            words[word] = None
            result +=  word + ' ' 
            
        # print('This is the result: ', result)
    return result.strip()

            




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))