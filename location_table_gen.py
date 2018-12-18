#LocationTable Generator
#Lap Yan Cheung, David Michael Acheampong

import nltk
import sys
from collections import defaultdict
from operator import itemgetter
from nltk.tag import pos_tag
from utils.util import punc, stop_words, pos_tags, get_pos, debug_path

def gen_location_table(sents, is_debug_mode):
    location_prep = ['on', 'at', 'in', 'to']
    location_table = defaultdict(int)
    #Generate location table:
    #   Use POS for conjunction, subordinating or preposition, read following word, if word is a
    #   determiner - read the one following it
    for sent in sents:
        tokens = nltk.word_tokenize(sent)
        for t in range(0, len(tokens)):
            if tokens[t].lower() in location_prep:
                if t+1 < len(tokens):
                    if get_pos(tokens[t+1]) == "DT":
                        if t+2 < len(tokens) and tokens[t+2] not in punc and get_pos(tokens[t+2])[0] == 'N':
                            location_table[tokens[t+2]] += 1
                    else:
                        if tokens[t+1] not in punc and get_pos(tokens[t+2])[0] == 'N':
                            location_table[tokens[t+1]] += 1
            else:
                continue

    if is_debug_mode:
        #Write table to file
        with open(debug_path + "locationFreq.txt", 'w') as location_file:
            #Sort dictionary by values
            for key, value in sorted(location_table.items(), key=itemgetter(1), reverse=True):
                location_file.write('%s\t%d\n' % (key, value))
        location_file.close()
    return location_table