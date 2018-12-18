# NLP FINAL PROJECT
by Lap Yan Cheung and David Acheampong

## Input File Word Frequency Table Generator
- This program creates and saves a Word Frequency Table from the input file to a .txt document "wordFreq.txt". In the document, the word and its number of instances are separated by a tab (\t)

## Character and Location Table Generators
- These programs create and save a Character and Location/Setting table derived from the input text, it uses NLTK POS_Tagger to determine Proper Nouns that are likely to also be names of characters in the story, as well as word tokens following prepositional words that are likely to be locations. The top 3 entries of both lists are printed to the output, in order to provide a more contextually-helpful summary of the input narrative text.

## Summarization Program
- This program takes a text file as input and summarizes it using the Word Frequency Table  program and outputs the summary into "summary.txt".

	
	- To run program:
		
		Type on command line
		
		"python summarizer.py <input file name>"
		
	- Optional flags: "-debug": outputs tables to text file, "-simp": replaces words with more commmon synonyms, "-loc": system uses location table, "-lemma": system lemmatizes words going in the word frequency table.
		
## Evaluation Program
- This program takes a system generated summary, a reference (human generated) summary and the source text that the summaries are based on as inputs. It calculates the compression rate as a percentage between the system summary and source text, and ROUGE scores calculated base on word overlaps between the system summary and the sample summary.

	- To run program:
	
		Type on the command line
		
		"python python3 summarization_evaluator.py <system summary file name> <reference summary file name> <source text>"

Rouge reference: http://www.aclweb.org/anthology/W04-1013, https://rxnlp.com/how-rouge-works-for-evaluation-of-summarization-tasks/#.XBVdjc9KiCQ

