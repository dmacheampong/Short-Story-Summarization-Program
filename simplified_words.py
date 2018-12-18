import nltk
import os
from nltk.corpus import wordnet
from nltk.corpus import brown
from collections import defaultdict
from nltk.probability import FreqDist
from utils.util import stop_words, get_pos, pos_tags, common_word_table, debug_path, punc

simp_word_dict = defaultdict(str)

def simplfy_word(word, character_table, is_debug_mode):
    new_word = word
    if word in simp_word_dict:
        new_word = simp_word_dict[word]
    elif get_pos(word) != 'NNP' and word not in character_table and word not in punc and word.lower() not in stop_words:
        highest_word_freq = 0
        if word in common_word_table:
            if get_pos(word)[0] == common_word_table[word][0]:
                highest_word_freq = int(common_word_table[word][1])
        for syn in wordnet.synsets(word):
            if get_pos(word)[0] in pos_tags:
                if '.' + pos_tags[get_pos(word)[0]] + '.' in syn.name():
                    syn_word = syn.lemmas()[0].name()
                    #print(word, syn_word)
                    if syn_word in common_word_table:
                        if highest_word_freq < int(common_word_table[syn_word][1]):
                            highest_word_freq = int(common_word_table[syn_word][1])
                            new_word = syn_word
        simp_word_dict[word] = new_word
    return new_word
    