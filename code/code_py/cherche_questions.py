#'C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv' pour pc portable

import pandas
import numpy

def telecharger_csv(lien):
    donnees = pandas.read_csv(lien, sep=',')
    donnees=donnees.as_matrix()
    return donnees
    
def questions(donnees,seuil):
    [n,m]=donnees.shape
    liste_question=[]
    for i in range (0,m):
        liste_reponses=[donnees[i,1]]#on initialise avec la première réponse
        for j in range (2,n):
            if donnees[j,i] not in liste_reponses:#on regarde si la réponse a déjà été donnée
                liste_reponses.append(donnees[j,i])
        #print(n)
        #print(len(liste_reponses))
        if not (len(liste_reponses)<):
            liste_question.append(i)
    return liste_question
            
    
def cherche_questions(lien,seuil):
    donnees=telecharger_csv(lien)
    return(questions(donnees))