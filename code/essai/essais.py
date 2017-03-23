#installer numpy et nltk en mode admin
import nltk

def corpus (lien):

    from nltk.corpus import PlaintextCorpusReader
    tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
    from nltk.corpus import PlaintextCorpusReader
    corpus_root = lien
    file_pattern = "discours.txt" 
    ptb = PlaintextCorpusReader(corpus_root, file_pattern)
    print(ptb.fileids())
    print(ptb.words('discours.txt'))
    
    
def tokenisation_mots (lien):#transforme en liste de mots le texte
    import re, pprint
    from nltk import word_tokenize
    f = open(lien) #ouverture texte
    texte = f.read()#lecture texte
    liste_mots=word_tokenize(texte) 
    return liste_mots
    
def tokenisation_phrases(lien):#transforme en liste de phrases le texte
    from nltk.tokenize import sent_tokenize
    f = open(lien) #ouverture texte
    texte = f.read()#lecture texte
    liste_phrases = sent_tokenize(texte)
    return liste_phrases

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
   # for x in structurePhrase: 
    #    if x[1] == 'NN' or x[1]=='NNP' or x[1]=='NNS' or x[1]== 
    #       liste_propre.append(mot)
   # return liste_propre
    return structurePhrase

def lireXML(xml):
    from lxml import etree
    tree = etree.parse(xml)
    for user in tree.xpath("/users/user/nom"):
    print(user.text)


#liste=tokenisation_mots("C:\\Users\\Paul\\Documents\\Ecole\\2A\\info\\projet\\projetS2\\code\\essai\\discours.txt")
phrases=tokenisation_phrases("C:\\Users\\Paul\\Documents\\Ecole\\2A\\info\\projet\\projetS2\\code\\essai\\discours.txt")
stop=stop_words(liste)
a=(structure(stop))
