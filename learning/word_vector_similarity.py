"""
        REMEMBER TO INSTALL spaCy and nlp LIBRARIES ON TERMINAL

        python -m pip install spacy
        python -m spacy download en_core_web_X  (X - sm/md/lg)

        https://realpython.com/natural-language-processing-spacy-python/
        https://www.youtube.com/watch?v=dIUTsFT2MeQ&t=3000s
"""

import spacy

nlp = spacy.load("en_core_web_md")


# WORD SIMILARITY
def show_similarity(base_word, textfile):

    base_token = nlp(base_word)
    doc = nlp(textfile)

    for token in doc:
        print(f"{token.text} <-> {base_token.text}:", token.similarity(base_token))


token_word = "bread"
texts = "I like eating egg mayo sandwich with crisps for lunch. However, I decided to go for hamburger today."
show_similarity(token_word, texts)

show_similarity("iPhone", "iPhone runs on iOS software. Samsung uses Android.")


print("\n")


# DOCUMENT SIMILARITY
doc1 = nlp("I like salty fries without tomato ketchup.")
doc2 = nlp("Fast food tastes very good but it is unhealthy.")
doc3 = nlp("I like cheeseburger more than hamburger.")

print(doc1, "<->", doc2, doc1.similarity(doc2))

# similarity by indexing
salty_fries = doc1[2:4]
hamburger = doc3[-2]

print(salty_fries, "<->", hamburger, salty_fries.similarity(hamburger))

