#!/usr/bin/env python3
import sys
Key_words = ["science","sea","fire"]

for line in sys.stdin:
    for keyword in Key_words:
        line = line.replace(keyword,"$")
        words = line.split()
        #print(words)
        try:
            if len(words) < 3:
                continue
            _index = words.index("$")
        except ValueError:
            continue
        #_index = int(words.index("$"))
        if _index >= 2 and _index <= (len(words)-1-2):
            print("%s_%s_%s\t1" % (words[_index-2],words[_index-1], words[_index] ))
            print("%s_%s_%s\t1" % (words[_index-1],words[_index], words[_index+1] ))
            print("%s_%s_%s\t1" % (words[_index],words[_index+1], words[_index+2] ))
        else:
             if _index == 0 :
                    print("%s_%s_%s\t1" % (words[_index],words[_index+1], words[_index+2] ))
             elif _index == 1:
                    print("%s_%s_%s\t1" % (words[_index],words[_index+1], words[_index+2] ))
                    print("%s_%s_%s\t1" % (words[_index-1],words[_index], words[_index+1] ))
             elif _index == len(words)-1 :
                     print("%s_%s_%s\t1" % (words[_index-2],words[_index-1], words[_index] ))
             elif _index == len(words) -1-1:
                     print("%s_%s_%s\t1" % (words[_index-2],words[_index-1], words[_index] ))
                     print("%s_%s_%s\t1" % (words[_index-1],words[_index], words[_index+1] ))
