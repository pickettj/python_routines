# -*- coding: utf-8 -*-

#Tokenizing Roshan Persian Digital Corpus
# Massive corpus of Persian literature, 
# pulled from Ganjur (http://ganjoor.net/) 
#by Roshan (https://persdigumd.github.io/PDL/)

import sys
sys.path.append('/Users/Enkidu/Documents/digital_humanities/python_routines/')

import arabic_cleaning as ac

import nltk, glob, bs4, pickle

#Globbing

files = glob.glob('/Users/Enkidu/Box Sync/Notes/Digital Humanities/Corpora/persian_literature_digital_corpus_roshan/data/**/*.xml', recursive=True)

#Assembling Corpus

raw_perslit_corpus = {}
for longname in files:
        f = open(longname)
        txt = f.read()
        f.close()
        start = longname.rindex('/')+1
        short = longname[start:-8]
        raw_perslit_corpus[short] = txt

        
#Cleaning Text

# pt. 1: strip html

nohtml_perslit = {}
for fn in raw_perslit_corpus:
    bstree = bs4.BeautifulSoup(raw_perslit_corpus[fn], 'lxml')
    nohtml_perslit[fn] = bstree.get_text()

# pt. 2: strip non-Arabic characters

clean_perslit = {fn: ac.clean_document(doc) for fn, doc in nohtml_perslit.items()}

    
#Tokenizing Text
 
perslit_toks = {}
for (fn, txt) in clean_perslit.items():
    toks = nltk.word_tokenize(txt)
    perslit_toks[fn] = toks
        

#Pickling

f = open("persian_lit_toks.pkl","wb")
pickle.dump(perslit_toks,f,-1)
f.close()


        
#clean_perslit['ferdousi.shahname.pdl'][5000:5800]
#perslit_toks['ferdousi.shahname.pdl'][50:70]