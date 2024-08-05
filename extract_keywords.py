import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pymorphy2


def extract_keywords(text):
    word_tokens = word_tokenize(text)
    keywords = [
        morph.parse(word)[0].normal_form
        for word in word_tokens
        if word not in stop_words and word not in string.punctuation
    ]
    return keywords


nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('russian'))
morph = pymorphy2.MorphAnalyzer()

# extract_keywords("На каком филиале есть курс по программированию?")
