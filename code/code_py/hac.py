#'C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv'
from nltk.probability import FreqDist
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
import pandas
import re, pprint
import numpy
from nltk import word_tokenize
from nltk.corpus import stopwords
from matplotlib import pyplot
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy as clust

liste_ponctuations=[',','?','!',';',':','.','(',')','"','[',']','/']
liste_declinaisons=['a','à', 'absolument', 'actuellement', 'ainsi', 'alors', 'apparemment', 'approximativement', 'après', 'après-demain', 'assez', 'assurément', 'au', 'aucun', 'aucunement', 'aucuns', 'aujourd’hui', 'auparavant', 'aussi', 'aussitôt', 'autant', 'autre', 'autrefois', 'autrement', 'avant', 'avant-hier', 'avec', 'avoir','beaucoup', 'bien', 'bientôt', 'bon','c\'est','c\'était','c\en', 'ça', 'car', 'carrément', 'ce', 'cela', 'cependant', 'certainement', 'certes', 'ces', 'ceux', 'chaque', 'ci', 'comme', 'comment', 'complètement','d\'y','d\'en', 'd\'abord', 'dans', 'davantage', 'de', 'début', 'dedans', 'dehors', 'déjà', 'demain', 'depuis', 'derechef', 'des', 'désormais', 'deux', 'devrait', 'diablement', 'divinement', 'doit', 'donc', 'dorénavant', 'dos', 'droite', 'drôlement', 'du','elle', 'elles', 'en', 'encore', 'enfin', 'ensuite', 'entièrement', 'entre-temps', 'environ', 'essai', 'est', 'et', 'étaient', 'état', 'été', 'étions', 'être', 'eu', 'extrêmement','fait', 'faites', 'fois', 'font','grandement', 'guère','habituellement', 'haut', 'hier', 'hors','ici', 'il', 'ils', 'infiniment', 'insuffisamment','jadis', 'jamais', 'je','j\'ai','j\'avais','j\'étais', 'j\en','j\'y','joliment','la', 'là', 'le', 'les', 'leur', 'leurs', 'lol', 'longtemps', 'lors','ma', 'maintenant', 'mais', 'mdr', 'même', 'mes', 'moins', 'mon', 'mot','naguère' ,'ne', 'ni','n\'y','n\'a','n\'en', 'nommés', 'non', 'notre', 'nous', 'nouveaux', 'nullement','ou', 'où', 'oui','par', 'parce', 'parfois', 'parole', 'pas', 'passablement', 'personne', 'personnes', 'peu', 'peut', 'peut-être', 'pièce', 'plupart', 'plus', 'plutôt', 'point', 'pour', 'pourquoi', 'précisément', 'premièrement', 'presque', 'probablement', 'prou', 'puis','quand', 'quasi', 'quasiment', 'que', 'quel', 'quelle', 'quelles', 'quelque', 'quelquefois', 'quels', 'qui', 'quoi','qu\'on', 'quotidiennement','rien', 'rudement','s\'en','s\'y', 'sa', 'sans', 'sans', 'ses', 'seulement', 'si', 'sien', 'sitôt', 'soit', 'son', 'sont', 'soudain', 'sous', 'souvent', 'soyez', 'subitement', 'suffisamment', 'sur','t\'y','t\'es','t\'en','ta', 'tandis', 'tant', 'tantôt', 'tard', 'te', 'tellement', 'tels', 'terriblement', 'tes', 'ton', 'tôt', 'totalement', 'toujours', 'tous', 'tout',' toutefois', 'très', 'trop', 'tu','un', 'une','valeur', 'vers', 'voie', 'voient', 'volontiers', 'vont', 'votre', 'vous', 'vraiment', 'vraisemblablement'] #pour compléter la liste des stop_words

def hac(numero_question):
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv')
    reponses=convertion_tableau(numero_question,donnees)
    reponses=linkage(reponses,'ward')
    reponses2=clust.fcluster(reponses, 5.6, criterion='distance')
    pyplot.title('Hierarchical Clustering Dendrogram (truncated)')
    pyplot.xlabel('sample index')
    pyplot.ylabel('distance')
    dendrogram(
    reponses,
    truncate_mode='lastp',  # show only the last p merged clusters
    p=5,  # show only the last p merged clusters
    show_leaf_counts=False,  # otherwise numbers in brackets are counts
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,  # to get a distribution impression in truncated branches
)
    pyplot.show()
    
    return reponses2
        
def telecharger_csv(lien):
    donnees = pandas.read_csv(lien, sep=',')
    donnees=donnees.as_matrix()
    return donnees
    
def convertion_tableau (numero_question,matrice):
    liste_cle=[] 
    matrice=matrice[:,numero_question]
    nb_reponses=matrice.shape[0]-1
    for i in range (1,nb_reponses):
        phrase=str(matrice[i])
        liste_mots= word_tokenize(phrase)  # transforme phrase en liste de mots
        for mot in liste_mots: 
            if mot.lower() not in stopwords.words('french') and mot not in liste_ponctuations and mot!='nan' and mot.lower() not in liste_declinaisons and mot.lower() not in liste_cle:
                liste_cle.append(mot)
    

    nb_mots=len(liste_cle)
    print(nb_reponses)
    tableau=numpy.zeros((nb_reponses,nb_mots))          
    for i in range (1,nb_reponses):
        phrase=str(matrice[i])
        liste_mots= word_tokenize(phrase)
        for j in range(nb_mots):      # transforme phrase en liste de mots
            tableau[i,j]=liste_mots.count(liste_cle[j])   
    return (tableau)