#!/usr/bin/env python
import sys
word_dict = {}
file = "doc"
for line in sys.stdin:
	word_plus_count={}
	word = line.split(",")[0].split("@")[0]
	#print(word)
	# word = line.split(",")[0]
	document = line.split(",")[0].split("@")[1]

	if word not in word_dict:
		word_plus_count[word] = 1
		word_plus_count[file] = document
		word_dict[word] = word_plus_count
		#print( word_dict[word],"\n")
	else:
		word_dict[word][word] =  word_dict[word][word] + 1
		

# print(word_dict,"\n")

for each in word_dict.items():
	sys.stdout.write(("{0}@{1},{2}\n".format(each[0],each[1]['doc'],each[1][each[0]])))
		# sys.stdout.write(("{0}\n".format(each[1][each[0]])))

	# sys.stdout.write(("{0}@{1},{2}\n".format(word, filename, 1)))
