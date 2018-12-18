#Frequency Table Generator 
#Lap Yan Cheung, David Michael Acheampong

import nltk
import os
import sys
from collections import defaultdict
from operator import itemgetter
from nltk.stem import WordNetLemmatizer
from utils.util import stop_words, debug_path, get_lemma

def gen_freq_table(sents, is_using_lemmas, is_debug_mode):
    freq_table = defaultdict(int)
    #Generate frequency table
    for sent in sents:
        tokens = nltk.word_tokenize(sent)
        for t in tokens:
            if t.isalpha() and t.lower() not in stop_words:
                if is_using_lemmas:
                    freq_table[get_lemma(t)] += 1
                else:
                    freq_table[t] += 1

    if is_debug_mode:
        #Write table to file
        with open(debug_path + 'word_freq.txt', 'w') as freq_file:
            for key, value in sorted(freq_table.items(), key=itemgetter(1), reverse=True):
                freq_file.write('%s\t%d\n'%(key, value))
        freq_file.close()
        if is_using_lemmas:
            with open(debug_path + 'word_lemmas.txt', 'w') as lemma_file:
                for sent in sents:
                    tokens = nltk.word_tokenize(sent)
                    for t in tokens:
                        if t.isalpha() and t.lower() not in stop_words:    
                            if t != get_lemma(t):
                                print('%s\t%s' % (t, get_lemma(t)), file = lemma_file)
            lemma_file.close()    
    return freq_table
