#!/usr/bin/python
from textblob.blob import TextBlob

b = TextBlob('Hola Amigo')
print b.detect_language()
