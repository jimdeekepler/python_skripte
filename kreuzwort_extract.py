#!/usr/bin/env python

import os
import sys

def extract_words(data):
    words = list()
    segments = [w.split() for w in data]
    #print(segments)
    for segment in segments:
        #print(segment)
        for w in segment:
            #print(w)
            if len(w) > 1:
                words.append(w.lower())
                #print(words)
    return words
    #words = [w.split() for w in data]
    #return words
    # TKT: Rest war alles Quatsch!
    #print("segments")
    #print(segments)
    #print()

    #words = [w for w in segments if len(w) > 1]

    #print("words")
    #print(words)
    #print()
    #return words
    ##word = [w for w in words if len(w) > 1]
    ## TODO: das raff ichnohc nicht. das liefert eine Liste von 
    ##  string zurück. da sind auch '1 char' strings dabei
    ##return word

def now_print(orientation, words):
    print("\nRichtung: " + orientation)
    for f in data:
        print(f)
        #if len(f) > 1:
        #    print(f)

# alternative: generator
# see [here](
#   https://stackoverflow.com/questions/3013449/list-comprehension-vs-lambda-filter?r=SearchResults)
#
def get_words(data):
    for w in data:
        if len(w) > 1: yield w


### main
with open("kreuzworträtsel_1.txt", "r") as f:
    data = list(f)

#print(len(data))
#print(data)
x = data.pop(0).strip()
y = data.pop(0).strip()

size_x = int(x)
size_y = int(y)

while len(data) > size_y:
    data.pop(0)

data = [d.rstrip('\r\n') for d in data]
data_t = [''.join(s) for s in zip(*data)]

#print(len(data))
#print(data)
#for f in extract_words(data):
#    print(f)
data = extract_words(data)
now_print("Waagrecht", data)

#print(data_t)
data = extract_words(data_t)
now_print("Senkrecht", data_t)

