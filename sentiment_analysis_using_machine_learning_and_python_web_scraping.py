# -*- coding: utf-8 -*-
"""Sentiment Analysis Using Machine Learning and Python/WEB SCRAPING

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18xJjEjp-TNrdH0HJncFCks5hGsVtsSda

GETTING SENTIMENT TEXT FROM WEBSITE
"""

pip install newspaper3k

from textblob import TextBlob
import nltk
from newspaper import Article

"""## GET THE ARTICLE"""

url = 'https://everythingcomputerscience.com'
article = Article(url)

article.download()            ## NLP
article.parse()
nltk.download('punkt')
article.nlp()

text = article.summary                ##  Get the Summary of the Article
text

## CREATE A TEXTBLOB OBJ

obj = TextBlob(text)

sentiment = obj.sentiment.polarity ## This return a value between -1 and 1
sentiment

if sentiment == 0:
  print('The text is neutral')
elif sentiment > 0:
  print('The text is Positive')
else:
  print('The text is Positive')