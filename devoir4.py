# coding: utf-8

import csv, spacy
from collections import Counter

tal = spacy.load("fr_core_news_md")

martino = "martino.csv"

f = open(martino)
chroniques = csv.reader(f)
next(chroniques)

tousMots = []
bigrams = []

# Boucle permettant de lemmatiser les mots des chroniques de M. Martineau.
for chronique in chroniques: 
    # print (chronique[3])
    doc = tal(chronique[3])
    tokens = [token.text for token in doc]
    for token in doc: 
        # print(token.text)
        lemmas = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    for lemma in lemmas: 
        tousMots.append(lemma)
    # print(len(bigrams))
    for x, y in enumerate(lemmas[:-1]):
        if "islam*" or "musul" in lemmas:
            bigrams.append("{} {}".format(lemmas[x], lemmas[x+1]))

    # print(bigrams)

# C'est ici que devraient s'afficher les 50 paires. Malheureusement, je ne peux le vérifier pour des raisons d'encodage sur PC. :(
freq = Counter(bigrams)
print(freq.most_common(51))