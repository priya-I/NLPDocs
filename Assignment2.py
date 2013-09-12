from nltk.book import *

#This line returns words with hyphen and the word 'index' in them. The position of these two elements is irrelevant
print sorted([w for w in set(text7) if '-' in w and 'index' in w])

#This line returns the words in the text that have title case and whose length is > 10 
print sorted([wd for wd in set(text3) if wd.istitle() and len(wd) > 10])

#This line returns the words in sent7 that are not in lower case. This means it will all the words where all the letters are not lower case.
print sorted([w for w in set(sent7) if not w.islower()])

#This line returns all the words that have 'cie' or 'cei' in them Eg: receive, society etc.
print sorted([t for t in set(text2) if 'cie' in t or 'cei' in t])

#Other commands
#Printing the frequency distribution of words in text1 and text2 that end with 'ing' and have 'cie' or 'cei' in them
fd1=FreqDist([w for w.upper() in text1 if w.endswith('ing') and ('cei' in w or 'cie' in w)])
print fd1

fd2=FreqDist([w for w.upper() in text2 if w.endswith('ing') and ('cei' in w or 'cie' in w)])
print fd2
