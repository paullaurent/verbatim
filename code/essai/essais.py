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
    f = open(lien)
    raw = f.read()
    liste=word_tokenize(raw)
    print(type(liste))
    print(liste)
    return liste
    
    
def stop_words(liste_mots):
    from nltk.corpus import stopwords
    for mot in liste_mots: 
        if mot.lower() in stopwords.words('french'):
           liste_mots.remove(mot)
    return liste_mots

