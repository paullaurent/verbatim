#'C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv'
import csv
import pandas
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
        
def nettoyer_csv(matrice):
    for x in matrice:
        if (x=='nan'):
            delete(matrice,x)
    return matrice