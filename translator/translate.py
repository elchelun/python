#!/usr/bin/python
from textblob.blob import TextBlob
from argparse import ArgumentParser
# encoding=utf8, I needed cuz asc 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

parser = ArgumentParser(description="Translator")
parser.add_argument("-f", "--file", dest="file", default="translate_file.txt", 
                    help="This is the file that needs traduction")
parser.add_argument("-w", "--word", dest="word", 
                    help="This is the word that needs traduction")
parser.add_argument("-e", "--english", 
                    action="store_true", dest="english", default=False, 
                    help="This will translate to ENGLISH")
parser.add_argument("-s", "--spanish", 
                    action="store_true", dest="spanish", default=False, 
                    help="This will translate to SPANISH")
options = parser.parse_args()

#print parser.parse_args()
#print options.word
def word_translator(words):
    b = TextBlob(words)
    if b.detect_language() == "en":
        print "The word " + words + " is in english and means",\
                b.translate(to="es") 
    elif b.detect_language() == "es":
        print "La palabra " + words +\
                " esta en espanol y en ingles significa", b.translate(to="en")
    return

def file_translator(file, language):
    with open(file, 'r') as fh:
        for f in fh:
            sentense = TextBlob(f)
            if language == "english":
                print sentense.translate(to="en")
            else:
                print sentense.translate(to="es")
    return

if options.word:
    word_translator(options.word)
elif options.file and options.english:
    file_translator(options.file, "english")
elif options.file and options.spanish:
    file_translator(options.file, "spanish")
else:
    print "No word or file entered for translation"
    print "Please use -h for help"
