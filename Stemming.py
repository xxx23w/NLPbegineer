# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:19:44 2022

@author: Isha Sharma
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords



paragraph = """“I have three visio
ns for India. ... I believe that Indi
a got its first vision of this in 1857,
 when we started the War of Independenc
 e. It is this freedom that we must pr
 otect and nurture and build on. If we 
 are not free, no one will respect us.
 My second vision for India's development
 """
 
 sentence = nltk.sent_tokenize(paragraph)
 stemmer = PorterStemmer()
 
 for i in range(len(sentence)):
     words = nltk.word_tokenize(sentence[i])
     words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
     sentence[i] = ' '.join(words)
 
 
