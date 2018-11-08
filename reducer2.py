#!/usr/bin/env python
import sys
word_dict = {}
n=0
c=0
a=sys.stdin
dict2={}
doc = "file"
for line in sys.stdin:
    dict3={}
    num = line.split(",")[1].split("=")[1]
    document = line.split(",")[0]
    word = line.split("=")[0].split(",")[1]
    if word not in dict3:
        word_dict[word] = int(num)
        n+=int(num)
        c+=1
        dict3[word]=int(num)
        dict3[doc] = document
        dict2[word]= dict3
    # else:
    #     word_dict[word] += int(num)
    #     n+=int(num)

for each in dict2.items():
    document=each[1]["file"]
    num=each[1][each[0]]
    word=each[0]
    sys.stdout.write("{0}@{1},{2}\n".format(document, word, num/n))
# for line1 in sys.stdin:
#     print("jhvj")
#     num = line1.split(",")[1].split("=")[1]
#     document = line1.split(",")[0]
#     word = line1.split("=")[0].split(",")[1]
#     print(num/n)
#     sys.stdout.write("{0},{1}={2}".format(document, word, num/n))
    

    #word = line.strip().split(",")[1].split("=")[0]
   # total_word = word_dict[document]
   # frequency = float(num)/total_word
        #print(word_dict)
    #niow3   sys.stdout.write("{0}@{1}\n".format(document_word, frequency))
        # sys.stdout.write("{0},{1}={2}".format(document, word, num))
# 
    #sys.stdout.write("{0},={1}".format(document_word, num))
