'''
Created on Sep 7, 2013

@author: Priya Iyer
'''

from nltk.book import *
import matplotlib
'''Part 1: All activities marked 'Your Turn' (YT)'''

#YT 1 Simple operations
x=2*(4+6)/1000
print x
print '************************************\n'

#YT 2 Searching for other words in the text using concordance
print "Searching for other words in the text using concordance:"
text1.concordance("survived") 
print '************************************\n'
text2.concordance("affection") 
print '************************************\n'
text3.concordance("lived") 
print '************************************\n'
text4.concordance("terror") 
print '************************************\n'
text5.concordance("rofl")
print '************************************\n'

#YT 3 Searching for similar words 
print "Searching for similar words as \'rise\' in text5 and text 7"
text7.similar("rise")
print '************************************\n'
text5.similar("rise")
print '************************************\n'
print "Common context in the words duty and failure found in the inaugral address text"
text7.similar("rise")
text4.common_contexts(["duty","failure"])
print '************************************\n'

#YT 4 How many times does lol appear in text5?
print "\"lol\" appears "+str(text5.count("lol"))+" times"
print "The percentage of 'lol' is: "+ str(100*text5.count("lol")/len(text5))
print '************************************\n'

#YT 5 Frequency distribution of text2
fdist2=FreqDist(text2)
print "Frequency Distribution of text2 is: "
print fdist2
print '************************************\n'

#YT 6 Fine grained selection of words
print "Fine grained selection of words"
V=set(text5)
long_words= [w for w in V if len(w)>15]
sort_list=sorted(long_words)
print sort_list
print '************************************\n'


'''Part 2: Writing a function that takes in a text object as input and a word (list) and
 prints out the text's name, , the total number of words in the text, the size of the vocabulary, 
 how often the word(s) occurs in the text, the concordance for the word(s), and plots the dispersion of the word(s) in the text.'''
def textalyzer(text,words):
    print 'The name of the text is: '
    print text
    print 'The total number of words in the text are: '+str(len(text))
    print 'The size of the vocabulary in the text is: '+str(len(set(text)))
    fdist=FreqDist(text)
    print words[0]+' occurs '+ str(fdist[words[0]])+' times in the text'
    print words[1]+' occurs '+ str(fdist[words[1]])+' times in the text'
    print words[2]+' occurs '+ str(fdist[words[2]])+' times in the text'
    print 'The concordance of the words \"'+words[0]+'\" is '
    print text.concordance(words[0])
    print 'The concordance of the words \"'+words[1]+'\" is '
    print text.concordance(words[1])
    print 'The concordance of the words \"'+words[2]+'\" is '
    print text.concordance(words[2])
    text.dispersion_plot(words)
    

textalyzer(text4,['country','nation','America'])
