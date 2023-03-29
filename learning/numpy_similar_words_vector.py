# ref: https://www.youtube.com/watch?v=dIUTsFT2MeQ&t=3000s
#      http://spacy.pythonhumanities.com/01_03_word_vectors.html (3.1.3)
# use numpy library

import spacy
import numpy as np

nlp = spacy.load("en_core_web_md")

doc = nlp("iPhone runs on iOS software. Samsung uses Android.")
my_word = "software"


# gives similar words to my_word from dictionary
ms = nlp.vocab.vectors.most_similar(np.asarray([nlp.vocab.vectors[nlp.vocab.strings[my_word]]]), n=10)

words = [nlp.vocab.strings[w] for w in ms[0][0]]

distances = ms[2]

print(words)