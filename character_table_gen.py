#CharacterTable Generator
#Lap Yan Cheung, David Michael Acheampong

import nltk
import sys
from collections import defaultdict
from operator import itemgetter
import os
import string
from utils.util import stop_words, punc, get_pos, debug_path

def gen_character_table(sents, is_debug_mode):
    character_table = defaultdict(int)
    #Generate character frequency table - Detecting capitalized words - likely proper nouns
    for sent in sents:
        tokens = nltk.word_tokenize(sent)
        #print(pos_tokens) #Debug
        last_word = ''
        for word in tokens:
            pos = get_pos(word)
            #Will overgenerate for now - will end word list to isolate names, not locations, etc.
            if pos == 'NNP' and word not in punc and word.lower() not in stop_words:
                #print(word)
                character_table[word] += 1
            elif pos[0] == 'V' and word not in stop_words:
                #Save words preceding a verb - likely names to character table
                character_table[last_word]+=1
            #Record last word if it is not a stop word or a punctuation
            if word not in stop_words and word not in punc:
                last_word = word
            #else:
                #last_word = ''
    if is_debug_mode:
        #Write table to file
        with open(debug_path + "character_freq.txt", 'w') as character_file:
            #Sort dictionary by values
            for key, value in sorted(character_table.items(), key=itemgetter(1), reverse=True):
                character_file.write('%s\t%d\n'%(key, value))
        character_file.close()
    return character_table
