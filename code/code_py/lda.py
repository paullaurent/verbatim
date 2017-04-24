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

liste_ponctuations=[',','?','!',';',':','.','(',')','"','[',']','/']
liste_declinaisons=['a','à', 'absolument', 'actuellement', 'ainsi', 'alors', 'apparemment', 'approximativement', 'après', 'après-demain', 'assez', 'assurément', 'au', 'aucun', 'aucunement', 'aucuns', 'aujourd’hui', 'auparavant', 'aussi', 'aussitôt', 'autant', 'autre', 'autrefois', 'autrement', 'avant', 'avant-hier', 'avec', 'avoir','beaucoup', 'bien', 'bientôt', 'bon','c\'est','c\'était','c\en', 'ça', 'car', 'carrément', 'ce', 'cela', 'cependant', 'certainement', 'certes', 'ces', 'ceux', 'chaque', 'ci', 'comme', 'comment', 'complètement','d\'y','d\'en', 'd\'abord', 'dans', 'davantage', 'de', 'début', 'dedans', 'dehors', 'déjà', 'demain', 'depuis', 'derechef', 'des', 'désormais', 'deux', 'devrait', 'diablement', 'divinement', 'doit', 'donc', 'dorénavant', 'dos', 'droite', 'drôlement', 'du','elle', 'elles', 'en', 'encore', 'enfin', 'ensuite', 'entièrement', 'entre-temps', 'environ', 'essai', 'est', 'et', 'étaient', 'état', 'été', 'étions', 'être', 'eu', 'extrêmement','fait', 'faites', 'fois', 'font','grandement', 'guère','habituellement', 'haut', 'hier', 'hors','ici', 'il', 'ils', 'infiniment', 'insuffisamment','jadis', 'jamais', 'je','j\'ai','j\'avais','j\'étais', 'j\en','j\'y','joliment','la', 'là', 'le', 'les', 'leur', 'leurs', 'lol', 'longtemps', 'lors','ma', 'maintenant', 'mais', 'mdr', 'même', 'mes', 'moins', 'mon', 'mot','naguère' ,'ne', 'ni','n\'y','n\'a','n\'en', 'nommés', 'non', 'notre', 'nous', 'nouveaux', 'nullement','ou', 'où', 'oui','par', 'parce', 'parfois', 'parole', 'pas', 'passablement', 'personne', 'personnes', 'peu', 'peut', 'peut-être', 'pièce', 'plupart', 'plus', 'plutôt', 'point', 'pour', 'pourquoi', 'précisément', 'premièrement', 'presque', 'probablement', 'prou', 'puis','quand', 'quasi', 'quasiment', 'que', 'quel', 'quelle', 'quelles', 'quelque', 'quelquefois', 'quels', 'qui', 'quoi','qu\'on', 'quotidiennement','rien', 'rudement','s\'en','s\'y', 'sa', 'sans', 'sans', 'ses', 'seulement', 'si', 'sien', 'sitôt', 'soit', 'son', 'sont', 'soudain', 'sous', 'souvent', 'soyez', 'subitement', 'suffisamment', 'sur','t\'y','t\'es','t\'en','ta', 'tandis', 'tant', 'tantôt', 'tard', 'te', 'tellement', 'tels', 'terriblement', 'tes', 'ton', 'tôt', 'totalement', 'toujours', 'tous', 'tout',' toutefois', 'très', 'trop', 'tu','un', 'une','valeur', 'vers', 'voie', 'voient', 'volontiers', 'vont', 'votre', 'vous', 'vraiment', 'vraisemblablement']

def telecharger_csv(lien):
    donnees = pandas.read_csv(lien, sep=',')
    donnees=donnees.as_matrix()
    return donnees

def programme_lda (numero_question,nb_sujets):
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv')
    texts=[]
    donnees=donnees[:,numero_question]
    for i in donnees :
        try:
            raw = i.lower()
        except:
            print("entier dï¿½tï¿½ctï¿½")
        tokens = word_tokenize(raw)
        stopped_tokens = [i for i in tokens if not i in stopwords.words('french') and i not in liste_ponctuations and i !='nan' and i not in liste_declinaisons] 
        stemmed_tokens = [PorterStemmer().stem(i) for i in stopped_tokens]
        texts.append(stemmed_tokens)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=nb_sujets, id2word = dictionary, passes=20)
    return(ldamodel.print_topics(num_topics=3, num_words=3))