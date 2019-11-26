# lab07_tests.py

# Brett Roach
# 6907380

from lab07 import totalWords

def test_totalWords_1():
    assert totalWords("input1.txt") == 11

def test_totalWords_2():
    assert totalWords("input2.txt") == 53

def test_totalWords_3():
    assert totalWords("input3.txt") == 5

from lab07 import longestWord

def test_longestWord_1():
    assert longestWord("input1.txt") == 'Finished'

def test_longestWord_2():
    assert longestWord("input2.txt") == 'midichlorians'

def test_longestWord_3():
    assert longestWord("input3.txt") == '14aaaaaaaaaaaa'

from lab07 import charactersPerWord

def test_charactersPerWord_1():
    assert charactersPerWord("input1.txt") == 4.818181818181818

def test_charactersPerWord_2():
    assert charactersPerWord("input2.txt") == 4.037735849056604

def test_charactersPerWord_3():
    assert charactersPerWord("input3.txt") == 10.0

from lab07 import wordFrequency

def test_wordFrequency_1():
    d = wordFrequency("input2.txt")
    assert d.get('Did') == 1

def test_wordFrequency_2():
    d = wordFrequency("input2.txt")
    assert d.get('Plagueis') == 2

def test_wordFrequency_3():
    d = wordFrequency("input2.txt")
    assert d.get('the') == 6

from lab07 import mostCommonWords

def test_mostCommonWords_1():
    assert mostCommonWords("input2.txt", 0) == []

def test_mostCommonWords_2():
    assert mostCommonWords("input2.txt", 1) == ['to']

def test_mostCommonWords_3():
    assert mostCommonWords("input2.txt", 5) == ['to', 'the', 'a', 'so', 'Sith']
