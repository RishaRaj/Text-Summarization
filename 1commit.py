# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:18:21 2020

@author: Risha Raj
"""

#importing required libraries
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
import os

def read_file(path):
    file = open(path)
    file.seek(0)
    file_content = file.read()
    file.close()
    return file_content

#file_content

def create_frequency_table(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    frequency_table = dict() 
    for word in words: 
        word = word.lower() 
        if word in stop_words: 
            continue
        if word in frequency_table: 
            frequency_table[word] += 1
        else: 
            frequency_table[word] = 1
    return frequency_table


#frequency_table


def create_score_dict(text):
    Tokenized_Sents = sent_tokenize(text) 
    Sent_Value_Dict = dict()
    frequency_table = create_frequency_table(text)
    Frequency_dict = frequency_table.items()
    
    for sent in Tokenized_Sents: 
        for word, frequency in Frequency_dict: 
            if word in sent.lower(): 
                if sent in Sent_Value_Dict: 
                    Sent_Value_Dict[sent] += frequency 
                else: 
                    Sent_Value_Dict[sent] = frequency
    return Sent_Value_Dict

def Calculate_Average(text):
    Sent_Value_Dict = create_score_dict(text)
    
    sumValues = 0
    for sentence in Sent_Value_Dict:
        sumValues += Sent_Value_Dict[sentence] 
    Avg = int(sumValues / len(Sent_Value_Dict))
    
    return Avg


file_name = "input_text.txt"
input_file = os.getcwd() + "\\" + file_name
file_content = read_file(input_file)
frequency_table = create_frequency_table(file_content)
Sent_Value_Dict = create_score_dict(file_content)
Average = Calculate_Average(file_content)