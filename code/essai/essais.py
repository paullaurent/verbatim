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



#liste=tokenisation_mots("C:\\Users\\Paul\\Documents\\Ecole\\2A\\info\\projet\\projetS2\\code\\essai\\discours.txt")
#phrases=tokenisation_phrases("C:\\Users\\Paul\\Documents\\Ecole\\2A\\info\\projet\\projetS2\\code\\essai\\discours.txt")
#stop=stop_words(liste)
#a=(structure(stop))

from nltk.tokenize import RegexpTokenizer
 #from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = stopwords.words('english')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health." 

# compile sample documents into a list
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]
print(texts)
print(corpus)
# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
print (ldamodel)



    
#def ligne_questions (tableau): #recherche des questions. On peut se permettre une complexité en n^4 puisque la recherche se termine vite
 #   for colonne in tableau:
  #      for phrase in colonne:
   #         for caractere in phrase:
    #            if caractere=="?":
     #               return colonne
                    
                    
#def liste_questions (tableau):
 #   questions=[]
  #  phrase_precedente="?"
   # for phrase in tableau:
    #    if not not phrase:
     #       if phrase[len(phrase)-1]=="?" and phrase_precedente[len(phrase_precedente)-1]=="?":
      #          questions.append(phrase)
       #     elif phrase[len(phrase)-1]=="?" and phrase_precedente[len(phrase_precedente)-1]!="?":
        #        x=phrase[0].lower()
         #       phrase[0]=x
          #      questions.append(phrase_precedente+' ,'+phrase)
           # phrase_precedente=phrase
    #return questions
    
#def tokenisation_mots (chaine_caractere):#transforme en liste de mots la réponse
 #   return word_tokenize(chaine_caractere) 