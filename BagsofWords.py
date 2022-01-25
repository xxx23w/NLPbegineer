# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:13:57 2022

@author: Isha Sharma
"""
import nltk
paragraph = """I have three visio
ns for India. ... I believe that Indi
a got its first vision of this in 1857,
 when we started the War of Independenc
 e. It is this freedom that we must pr
 otect and nurture and build on. If we 
 are not free, no one will respect us.
 My second vision for India's development
 """
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet=WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]',' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()


    
