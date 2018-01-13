"""
This class used to calculate Flesch-Kincaid Reading Grade.
Only support english articles

Library: nltk , re
Author: Jie Tao
Time: 2018-01-12
"""

import nltk
import re

class FKCalcu:
    def __init__(self,text):
        self.__text = text;           # input article - english only
        self.__sentenceCount = 0;     # sentences token
        self.__wordCount = 0;         # word token
        self.__syllCount = 0;         # syllables token
        self.__grade = 0;             # grade
        self.__re_words = re.compile(r'\w+', flags=re.UNICODE)    # regular expression for words

    # Tokenize the sentence by nltk
    def __getTokenNum(self):
        sentList = nltk.sent_tokenize(self.__text,
                                        language="english")     # sentece list
        self.__sentenceCount = len(sentList)                      # num of sentence

        for sentence in sentList:                               # internative each sentence in list
            wordList = self.__re_words.findall(sentence)
            self.__wordCount += len(wordList)

            for word in wordList:                               # iternative each word in sentence
                self.__syllCount += self.__getSyllCount(word)

    # Calculate Flesch-Kincaid Reading Ease
    # 206.835 - 1.015*(total words/total sentences)-84.6(total syllables/total words)
    def calFKGrade(self):
        self.__getTokenNum()
        self.__grade = 206.835 - 1.015 * (self.__wordCount/self.__sentenceCount) \
                        - 84.6 * (self.__syllCount/self.__wordCount)


    # Count the syllable in a word
    # each incontinuity vowel will be count as a syllable except end with letter 'e'
    def __getSyllCount(self, word):
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1

        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
                if word.endswith("e"):
                    count -= 1

        if count == 0:
            count += 1

        return count

    @property
    def totalWords(self):
        return self.__wordCount

    @property
    def totalSentence(self):
        return self.__sentenceCount

    @property
    def totalSyllables(self):
        return self.__syllCount

    @property
    def avgword(self):
        return self.__wordCount/self.__sentenceCount

    @property
    def avgSyllables(self):
        return self.__syllCount/self.__wordCount

    @property
    def grade(self):
        return self.__grade
