
def corpus (lien):
    import nltk
    from nltk.corpus import PlaintextCorpusReader
    tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
    from nltk.corpus import PlaintextCorpusReader
    corpus_root = lien
    file_pattern = "discours.txt" 
    ptb = PlaintextCorpusReader(corpus_root, file_pattern)
    print(ptb.fileids())
    print(ptb.words('discours.txt'))
    
    
def tokenisation (lien):
    import nltk, re, pprint
    from nltk import word_tokenize
    f = open(lien) #ouverture texte
    raw = f.read()#lecteure texte
    liste=word_tokenize(raw) #transforme en liste de mots le texte
    print(type(liste))
    #print(liste)
    return liste

liste_ponctuations=[',','?','!',';',':','.']
def stop_words(liste_mots):
    from nltk.corpus import stopwords
    liste_propre=[]  #obligé de passer par une liste parallèle car python gère mal la suppression des éléments de la liste lors de son parcours
    for mot in liste_mots: 
        if mot.lower() not in stopwords.words('french') and mot not in liste_ponctuations:
           liste_propre.append(mot)
    return liste_propre


def structure(liste):
    from nltk import tag
    structurePhrase = tag.pos_tag(liste)
    return structurePhrase



liste=tokenisation("C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\essai\\discours.txt")
a=(structure(liste))
