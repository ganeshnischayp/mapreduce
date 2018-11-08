#!/usr/bin/env python
import sys
import math
dict_word = {}
dict_word_doc = {}
D = 12
for line in sys.stdin:
    word_in_doc = line.strip().split("=")[0]
    freq = line.strip().split("=")[1]
    #freq is the frequency of the word in that document
    dict_word_doc[word_in_doc] = freq
    word = line.strip().split(",")[0]
    #used to determine in how many docs we are having this word
    if word in dict_word:
        dict_word[word] += 1
    else:
        dict_word[word] = 1
for element in dict_word_doc:
    document = element.split(",")[1]
    word = element.split(",")[0]
    d = dict_word[word]
    tf = math.log(float(D)/float(d))
    freq = float(dict_word_doc[element])
    tfidf = tf*float(freq)
    sys.stdout.write("{0}@{1},{2},{3},{4}\n".format(word, document, tf, freq, tfidf))
