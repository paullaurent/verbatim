#'C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv' pour pc portable
#'C:\\Users\\Paul\\Documents\\Ecole\\2A\\info\\projet\\projetS2\\code\\code_py\\csv2.csv' pour fixe
import nltk
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
    
def ligne_questions (tableau): #recherche des questions. On peut se permettre une complexité en n^4 puisque la recherche se termine vite
    for colonne in tableau:
        for phrase in colonne:
            for caractere in phrase:
                if caractere=="?":
                    return colonne
                    
                    
def liste_questions (tableau):
    questions=[]
    phrase_precedente="?"
    for phrase in tableau:
        if not not phrase:
            if phrase[len(phrase)-1]=="?" and phrase_precedente[len(phrase_precedente)-1]=="?":
                questions.append(phrase)
            elif phrase[len(phrase)-1]=="?" and phrase_precedente[len(phrase_precedente)-1]!="?":
                x=phrase[0].lower()
                phrase[0]=x
                questions.append(phrase_precedente+' ,'+phrase)
            phrase_precedente=phrase
    return questions
            
def telecharger_csv(lien):
    donnees = pandas.read_csv(lien, sep=',')
    donnees=donnees.as_matrix()
    return donnees
        
def nettoyer_csv(matrice): #supprime les éléments vides des réponses
    for x in matrice:
        if str(x) == 'nan':
            numpy.delete(matrice,x)
    return matrice
    
def tokenisation_mots (chaine_caractere):#transforme en liste de mots la réponse
    liste_mots=word_tokenize(chaine_caractere) 
    return liste_mots
    
def analyser_reponse (numero_question,matrice):
    liste_cle=[]
    cool='cool'  
    matrice=matrice[:,numero_question]
    nb_reponses=matrice.shape[0]-1
    for i in range (1,nb_reponses):
        phrase=str(matrice[i])
        liste_mots= tokenisation_mots(phrase)
        for mot in liste_mots: 
            if mot.lower() not in stopwords.words('french') and mot not in liste_ponctuations:
                liste_cle.append(mot)
                   
    return liste_cle
    
def programme ():
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\Ecole\\2A\\info\\projet\\projetS2\\code\\code_py\\csv2.csv')
    donnees=nettoyer_csv(donnees)
    reponses=analyser_reponse(0,donnees)
    return reponses