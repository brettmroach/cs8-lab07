# lab07.py

# Brett Roach
# 6907380

def totalWords(filename):
    '''Returns the total number of words in the file'''
    infile = open(filename, 'r')
    text = infile.read()
    infile.close()
    for char in text:
        if char in ',.!?;':
            text = text.replace(char, ' ', 1)
    word_list = text.split()
    total_words = len(word_list)
    return total_words

def longestWord(filename):
    '''Returns the longest word in the text file'''
    infile = open(filename, 'r')
    word_list = infile.read().split()
    for i in range(len(word_list)):
        for char in word_list[i]:
            if char.isalnum() == False:
                word_list[i] = word_list[i].strip(char)
    for i in range(0, len(word_list)):
        for j in range(i+1, len(word_list)):
            if len(word_list[j]) > len(word_list[i]):
                word_list.insert(i, word_list.pop(j))
    return word_list[0]

def charactersPerWord(filename):
    '''Returns the average number of characters per word in the file'''
    infile = open(filename, 'r')
    word_list = infile.read().split()
    for i in range(len(word_list)):
        for char in word_list[i]:
            if char.isalnum() == False:
                word_list[i] = word_list[i].strip(char)
    t = 0
    for word in word_list:
        t += len(word)
    avg = t/(len(word_list))
    return avg

def wordFrequency(filename):
    '''Returns a dictionary with the frequency of each word in the
    file as its value.'''
    infile = open(filename, 'r')
    word_list = infile.read().split()
    for i in range(len(word_list)):
        for char in word_list[i]:
            if char.isalnum() == False:
                word_list[i] = word_list[i].strip(char)
    word_f = dict()
    for word in word_list:
        if word in word_f:
            word_f[word] = word_f[word] + 1
        else:
            word_f[word] = 1
    return word_f

def mostCommonWords(filename, N):
    '''returns a list of N most common words in the text file'''
    word_frequency = wordFrequency(filename)
    common_words = list(word_frequency.keys())
    for i in range(len(word_frequency)):
        a = common_words[i]
        for j in range(i+1, len(word_frequency)):
            b = common_words[j]
            if word_frequency[b] > word_frequency[a]:
                common_words.insert(i, common_words.pop(j))
    return common_words[0:N]




