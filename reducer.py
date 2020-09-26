#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None
topten = dict()
for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t", 1)
    try :
        count = int(count)
    except ValueError: 
        continue
    if current_word == word:
        current_count = current_count + count
    else : 
        if current_word :
            if len(topten) == 10 : 
            
                try : 
                    minval = min(topten.values())
                except ValueError : 
                    minval = 0
                if current_count > minval : 
                    minwords = [k for k in topten if topten[k] == minval]
                    del topten[minwords[0]]
                    topten[current_word]= current_count
            else : 
                topten[current_word]= current_count        
            #print("%s\t%s" % (current_word,current_count))
        current_count = count
        current_word = word
if current_word == word:
    minval = min(topten.values())
    if current_count > minval : 
        minwords = [k for k in topten if topten[k] == minval]
        del topten[minwords[0]]
        topten[current_word]= current_count
    #print ('%s\t%s' % (current_word, current_count))

for trigram, count in topten.items():
    print('%s\t%s' % (trigram, count))
