# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:35:32 2022

@author: Isha Sharma
"""

import nltk
from nltk.stem import WordNetLemmatizer
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


sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)



     
