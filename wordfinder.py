"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine to get random word from list of words.

    assume you have a file that looks like this:
        cat
        dog
        porcupine

    >>> wf = WordFinder("/Users/christien/github/Springboard-Assignments/18.4_python-oo-practice/words.txt")
    5 words read

    >>> wf.random()
    ''

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'
    
    >>> wf.random()
    '# comment'
    
    >>> wf.random()
    'dog'
    """

    def __init__(self, src):
        """initialize SerialGenerator with a start number"""
        file = open(src)
        self.words = self.count_words(file)
        print(f"{len(self.words)} words read")

    def count_words(self, file):
        """counts length of words in list"""
        return [word.strip() for word in file]

    def random(self):
        """return random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Does not return empty lines or # comments

    >>> swf = SpecialWordFinder("/Users/christien/github/Springboard-Assignments/18.4_python-oo-practice/words.txt")
    3 words read

    >>> swf.random()
    'cat'
    """

    def count_words(self, file):
        return [w.strip() for w in file
        if w.strip() and not w.startswith("#")]