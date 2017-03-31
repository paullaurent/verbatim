 # -*-coding:Latin-1 -* 
#'C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv' pour pc portable
#'C:\\Users\\Paul\\Documents\\Ecole\\2A\\info\\projet\\projetS2\\code\\code_py\\csv2.csv' pour fixe
#conda install -c anaconda gensim=1.0.1
#pip install owlready
from owlready import *
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
import gensim
from gensim import corpora, models
import csv
import pandas
import re, pprint
import numpy
from nltk import word_tokenize
liste_ponctuations=[',','?','!',';',':','.']
from nltk.corpus import stopwords
def lecture_csv(lien):
    tableau=[]
    reader=csv.reader(open(lien))
    for colonne in reader:
        tableau.append(colonne)
    return tableau

            
def telecharger_csv(lien):
    donnees = pandas.read_csv(lien, sep=',')
    donnees=donnees.as_matrix()
    return donnees

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
#def nettoyer_csv(matrice): 
   # for x in matrice :
      #  if str(x)=='nan':
     #       numpy.delete(x)
   # return matrice
    

    
    
def analyser_reponse (numero_question,matrice):
    liste_cle=[] 
    matrice=matrice[:,numero_question]
    nb_reponses=matrice.shape[0]-1
    for i in range (1,nb_reponses): 
        phrase=str(matrice[i])
        liste_mots= word_tokenize(phrase)  
        for mot in liste_mots: 
            if mot.lower() not in stopwords.words('french') and mot not in liste_ponctuations and mot!='nan': 
                liste_cle.append(mot)
                   
    return liste_cle
    
def mots_recurrents (reponses):
    liste_termes=[reponses[0]]
    liste_recurrences=[1]
    for i in range (1,len(reponses)):
        if reponses[i] not in liste_termes : 
                liste_termes.append(reponses[i])
                liste_recurrences.append(1)
        else:
            for j in range (0,len(liste_termes)):
                if reponses[i]==liste_termes[j]:
                    liste_recurrences[j]=liste_recurrences[j]+1 
    return liste_termes, liste_recurrences
    

def programme_freq (numero_question):
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv')
    try:
        reponses=analyser_reponse(numero_question,donnees)
        reponses=mots_recurrents(reponses)
        return reponses 
    except  :
        print ("Le numéro question est incorrect")
    
    
def programme_lda (numero_question):
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv')
    texts=[]
    donnees=donnees[:,numero_question]
    for i in donnees :
        try:
            raw = i.lower()
        except:
            print("entier détécté")
        tokens = word_tokenize(raw)
        stopped_tokens = [i for i in tokens if not i in stopwords.words('french') and i not in liste_ponctuations and i !='nan'] 
        stemmed_tokens = [PorterStemmer().stem(i) for i in stopped_tokens]
        texts.append(stemmed_tokens)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=20)
    print(ldamodel.print_topics(num_topics=3, num_words=3))
    
    
def telecharger_onto():
    onto_path.append("C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\")
    onto.load()
    return onto
