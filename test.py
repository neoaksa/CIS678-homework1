import nltk
import re

__re_words = re.compile(r'\w+', flags=re.UNICODE)
__sentList = nltk.sent_tokenize("maybe custom tokenize language not available on fs. I love python.")

for word in __sentList:
    wordList = __re_words.findall(word)
    print(len(wordList))


