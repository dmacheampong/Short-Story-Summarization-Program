#Stop words from nltk corpus
#David Michael Acheampong, Lap Yan Cheung

import csv
import nltk
from collections import defaultdict
from nltk.stem import WordNetLemmatizer

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours',
'ourselves', 'you', 'you\'re', 'you\'ve', 'you\'ll', 'you\'d',
'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
'himself', 'she', 'she\'s', 'her', 'hers', 'herself', 'it', 'it\'s',
'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
'which', 'who', 'whom', 'this', 'that', 'that\'ll', 'these', 'those', 'am',
'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having',
'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because',
'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'don\'t', 'should',
'should\'ve', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'aren\'t',
'couldn', 'couldn\'t', 'didn', 'didn\'t', 'doesn', 'doesn\'t', 'hadn', 'hadn\'t',
'hasn', 'hasn\'t', 'haven', 'haven\'t', 'isn', 'isn\'t', 'ma', 'mightn', 'mightn\'t',
'mustn', 'mustn\'t', 'needn', 'needn\'t', 'shan', 'shan\'t', 'shouldn', 'shouldn\'t',
'wasn', 'wasn\'t', 'weren', 'weren\'t', 'won', 'won\'t', 'wouldn', 'wouldn\'t', '\'s']

sum_path = 'summaries/'
debug_path = 'debugging/'

punc = ['.', ',', ';', '?' , '!', "'", '"', '\u2018', '\u2019', '\u201C', '\u201D']
pos_tags = {'N': 'n', 'J': 'a', 'V': 'v', 'R': 'r'}
word_freq_file = open('utils/word_freq_data.txt', 'r')

file_reader = csv.reader(word_freq_file)
common_word_table = defaultdict(list)
for w, p, f in file_reader:
    common_word_table[w] = [p, f]

def get_pos(word):
    return nltk.pos_tag(word)[0][1]

#Not in use
def get_lemma(word):
    lemmatizer = WordNetLemmatizer()
    if get_pos(word)[0] in pos_tags:
        word = lemmatizer.lemmatize(word, pos=pos_tags[get_pos(word)[0]])
    return word
