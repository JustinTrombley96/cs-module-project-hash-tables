# Your code here
def count_words(file):
    ignored_characters = '\:",.-+=/\|[]{}()*^&'

    word_map = {}

    with open(file) as f:
        words = f.read().lower()
        for char in ignored_characters:
            words = words.replace(char, "")
        words = words.split()

        for word in words:
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] += 1
        return word_map

def render_word_count(dic):
    counts = [(dic[word], word) for word in dic]
    counts.sort(key = lambda e: (-e[0], e[1]))
    maxLength = 0

    for word in counts:
        if len(word[1]) > maxLength:
            maxLength = len(word[1])
        
    for word in counts: 
        print(f'{word[1]}\t'.expandtabs(maxLength + 2) + '#' * word[0])
    
render_word_count(count_words("robin.txt"))