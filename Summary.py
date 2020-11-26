# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:30:01 2020

@author: Risha Raj
"""

# importing libraries 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
   
# Input text - to summarize  
text = """Just like the evolution of mankind, machines have also evolved over time. This has been possible due to the increased interaction between human and a machine. However, machines have never been able to completely understand the natural language of humans. NLP strives to achieve this. 

	NLP(Natural Language Processing) is the branch of Artificial Intelligence that helps computers understand and analyze natural language of humans in a meaningful and efficient way. Language is being the most basic form of interaction for humans. In order to understand human psychology better, it becomes extremely crucial for machines to understand natural language. This is to enhance the human-machine interaction experience. Hence, NLP is the need of the hour."""

# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 
   
# Creating a frequency table to keep the  
# score of each word 
   
freqTable = dict() 
for word in words: 
    word = word.lower() 
    if word in stopWords: 
        continue
    if word in freqTable: 
        freqTable[word] += 1
    else: 
        freqTable[word] = 1
   
# Creating a dictionary to keep the score 
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 
   
for sentence in sentences: 
    for word, freq in freqTable.items():
        #print('word', word, 'freq',freq)
        if word in sentence.lower(): 
            if sentence in sentenceValue: 
                sentenceValue[sentence] += freq 
            else: 
                sentenceValue[sentence] = freq
#print(len(sentenceValue))
   
   
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence] 
# Average value of a sentence from the original text 
   
average = int(sumValues / len(sentenceValue))
   
# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
        summary += " " + sentence 
#print(summary) 