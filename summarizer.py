#Text Summarizer
#David Michael Acheampong, Lap Yan Cheung

'''
TO-DO LIST for this week!!!
1. Add back the character info
'''

from collections import defaultdict
from freq_table_gen import gen_freq_table
from character_table_gen import gen_character_table
from location_table_gen import gen_location_table
from simplified_words import simplfy_word, simp_word_dict
from nltk.tokenize.treebank import TreebankWordDetokenizer
from operator import itemgetter
import csv
import math
import nltk
import sys
from utils import util
from utils.util import debug_path, sum_path, get_lemma
import os

is_debug_mode = False
is_simp_mode = False
is_using_locations = False
is_using_lemmas = False

def debug_info(character_table, sent_scores, avg_score):
    sentence_scores = ''
    #Output sentence score table for debugging
    for sent in sent_scores:
        sentence_scores += '%s\n%s\n\n' % (sent, sent_scores[sent])

    sentence_scores += '\nAverage Sentence Score: %s' % (avg_score)
    with open(debug_path + 'sentence_scores.txt', 'w') as sentence_score_output:
        print(sentence_scores, file=sentence_score_output)
    sentence_score_output.close()

    #Add character info
    characters_info = ''
    characters_info += "Characters:\n"
    count = 0
    #Write top characters from list to output
    for key, value in sorted(character_table.items(), key=itemgetter(1), reverse=True):
        characters_info += '%s\n' % (key)
        count +=1
        if count == 3:
            break
    return characters_info + '\n'

def debug_loc_info(location_table):
    count = 0
    location_info = ''
    #Write top locations retrieved to output
    location_info += "\nLocations:\n"
    for key, value in sorted(location_table.items(), key=itemgetter(1), reverse=True):
        location_info += '%s\n' % (key)
        count +=1
        if (count==3):
            break
    return location_info + '\n'

def summarize(sents):
    summary = ''
    freq_table = gen_freq_table(sents, is_using_lemmas, is_debug_mode) #Word frequency table
    character_table = gen_character_table(sents, is_debug_mode)
    if is_using_locations:
        location_table = gen_location_table(sents, is_debug_mode)
    sent_scores = defaultdict(int) #Stores sentences scores
    #Get sentence scores
    for sent in sents:
        for word in nltk.word_tokenize(sent):
            if is_using_lemmas:
                word = get_lemma(word)
            if word in freq_table:
                weight = 1
                if word in character_table:
                    weight = 2
                if is_using_locations:
                    if word in location_table:
                        weight = 1.5
                sent_scores[sent] += freq_table[word] * weight
        sent_scores[sent] /= len(sent)
    #Get average sentence score
    total_score = 0
    for sent in sent_scores:
        total_score += sent_scores[sent]
    avg_score = total_score / len(sent_scores)

    if is_debug_mode:
        summary += debug_info(character_table, sent_scores, avg_score) + '\n'
        if is_using_locations:
            summary += debug_loc_info(location_table) + '\n'
            
    selected_sents = []
    max_sent_num = 25
    scalar = 1
    idx = 0
    for sent in sents:
        if sent_scores[sent] > scalar * avg_score:
            sent_info = [sent, idx, sent_scores[sent]]
            selected_sents.append(sent_info)
        idx += 1

    if len(selected_sents) > max_sent_num:
        sorted_sents = sorted(selected_sents, key=itemgetter(2), reverse=True)
        selected_sents = []
        for i in range(0, max_sent_num):
            selected_sents.append(sorted_sents[i])
        selected_sents = sorted(selected_sents, key=itemgetter(1))

    for sent in selected_sents:
        if is_simp_mode:
            tokens = nltk.word_tokenize(sent[0])
            for i in range(0, len(tokens)):
                tokens[i] = simplfy_word(tokens[i], character_table, is_debug_mode)
            detokenizer = TreebankWordDetokenizer()
            simple_sent = detokenizer.detokenize(tokens)
            summary += simple_sent + '\n'

            if is_debug_mode:
                with open(debug_path + 'simple_words_table.txt', 'w') as simp_words_file:
                    for word in simp_word_dict:
                        if word != simp_word_dict[word]:
                            print('%s\t%s' % (word, simp_word_dict[word]), file=simp_words_file)
                simp_words_file.close()
        else:
            summary += sent[0] + '\n'
        summary = summary.replace(' \u2019 s', '\'s').replace(' \u201C', '"').replace('\u201D ' ,'"')
    return summary


#Reads and stores file contents
with open(sys.argv[1], 'r') as input_file:
    text = input_file.read()
input_file.close()

if '-debug' in sys.argv:
    is_debug_mode = True
    if not os.path.exists(debug_path):
        os.makedirs(debug_path)
if '-simp' in sys.argv:
    is_simp_mode = True
if '-loc' in sys.argv:
    is_using_locations = True
if '-lemma' in sys.argv:
    is_using_lemmas = True
        
sentences = nltk.sent_tokenize(text) #Sentences

summary_file_name = sys.argv[1].rpartition('/')[2].replace('.txt', '_summary')
if is_simp_mode:
    summary_file_name += '_simp'
if is_debug_mode:
    summary_file_name += '_debug'
if is_using_locations:
    summary_file_name += '_loc'
if is_using_lemmas:
    summary_file_name += '_lemma'
summary_file_name += '.txt'

if not os.path.exists(sum_path):
    os.makedirs(sum_path)

with open(sum_path + summary_file_name, 'w') as output_file:
    print(summarize(sentences), file=output_file)
util.word_freq_file.close()
output_file.close()

