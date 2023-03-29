"""
        REMEMBER TO INSTALL spaCy and nlp LIBRARIES ON TERMINAL

        python -m pip install spacy
        python -m spacy download en_core_web_X  (X - sm/md/lg)

        Referencesd: https://realpython.com/natural-language-processing-spacy-python/
                     https://www.youtube.com/watch?v=vyohzuTkty8&t=73s
"""

import spacy

nlp = spacy.load("en_core_web_md")


def show_similarity(base_word, textfile):

    base_token = nlp(base_word)
    doc = nlp(textfile)

    for token in doc:
        print(f"{token.text} <-> {base_token.text}:", token.similarity(base_token))


token_word = "bread"
texts = "I like eating egg mayo sandwich with crisps for lunch. However, I decided to go for hamburger today."

show_similarity(token_word, texts)

show_similarity("iPhone", "iPhone runs on iOS software. Samsung uses Android.")
