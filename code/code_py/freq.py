#!C:\Users\Paul\Anaconda3\python.exe
from flask import Flask
app = Flask(__name__)

@app.route("/")
numero_question=2
def programme_freq2():
    numero_question=2
    from nltk.probability import FreqDist
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
    from nltk.corpus import stopwords
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv')
    try:
        
        reponses=analyser_reponse(numero_question,donnees)
        #reponses=FreqDist(reponses)
        #print (reponses)
        return "ok" 
    except  :
        return ("Le numï¿½ro question est incorrect")  
        
def telecharger_csv(lien):
    import pandas
    import numpy
    donnees = pandas.read_csv(lien, sep=',')
    donnees=donnees.as_matrix()
    return donnees
    
def analyser_reponse (numero_question,matrice):
    from nltk.probability import FreqDist
    import nltk
    from nltk.tokenize import RegexpTokenizer
    from nltk.stem.porter import PorterStemmer
    import gensim
    from gensim import corpora, models
    import re, pprint
    import numpy
    from nltk import word_tokenize
    from nltk.corpus import stopwords
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
        


if __name__ == "__main__":
    app.run()
