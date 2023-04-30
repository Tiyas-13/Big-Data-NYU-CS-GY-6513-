#!/usr/bin/python

import sys
import re
import string
#
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    #
    l = re.sub('[' + string.punctuation + ']', '', line).split()
    #
    for i in range(len(l)-2):
        #
        # if i==0:
        #     bigram = "..., " + l[i]
        # else:
        #     bigram = l[i-1] + ", " + l[i]
        trigram = l[i] + ", " + l[i+1] + ", " + l[i+2]
        #
        print "%s\t%d" %(trigram, 1)
        # print(trigram,1)

    # print "%s\t%d" %(l[len(l)-1]+", ...", 1)
        #
        #
        #output goes to STDOUT (stream data that the program writes)
        #print "%s\t%d" %( bigram, 1 )

