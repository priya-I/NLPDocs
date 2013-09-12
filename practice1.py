from nltk.book import *
import re
'''
print "The name of the text is: "
print text4
print text3[-10:]
print sorted(sent1+sent2+sent3+sent4+sent5+sent6+sent7+sent8)
'''

print sorted([w for w in set(text3) if w.endswith('ing')])
print sorted([w for w in set(text4) if w.endswith('ing')])
fd5=FreqDist([w for w in text5 if w[-3:]=='ing'])
fd6=FreqDist([w for w in text6 if w[-3:]=='ing'])
#store lenghts in a list
lengths=[len(w) for w in set(text4)]


print '-'*90
print 'Frequent Word\t#of Occurrences\t Percent of total'
print '-'*90
fd=FreqDist([w for w in text2])
topten=fd.items()[:10]
print topten
