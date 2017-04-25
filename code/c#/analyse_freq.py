 # -*-coding:Latin-1 -* 
#'C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv' pour pc portable
#'C:\\Users\\Paul\\Documents\\Ecole\\2A\\info\\projet\\projetS2\\code\\code_py\\csv2.csv' pour fixe
#conda install -c anaconda gensim=1.0.1
#pip install owlready
#from owlready import *
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
liste_ponctuations=[',','?','!',';',':','.','(',')','"','[',']']
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

#def ligne_questions (tableau): #recherche des questions. On peut se permettre une complexit� en n^4 puisque la recherche se termine vite
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
def programme_freq2(numero_question):
    from nltk.probability import FreqDist
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv')
    try:
        reponses=analyser_reponse(numero_question,donnees)
        reponses=FreqDist(reponses)
        return reponses 
    except  :
        print ("Le num�ro question est incorrect")  

def programme_freq (numero_question):
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv')
    try:
        reponses=analyser_reponse(numero_question,donnees)
        reponses=mots_recurrents(reponses)
        return reponses 
    except  :
        print ("Le num�ro question est incorrect")
    
    
def programme_lda (numero_question,nb_sujets):
    donnees=telecharger_csv('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\csv2.csv')
    texts=[]
    donnees=donnees[:,numero_question]
    for i in donnees :
        try:
            raw = i.lower()
        except:
            print("entier d�t�ct�")
        tokens = word_tokenize(raw)
        stopped_tokens = [i for i in tokens if not i in stopwords.words('french') and i not in liste_ponctuations and i !='nan'] 
        stemmed_tokens = [PorterStemmer().stem(i) for i in stopped_tokens]
        texts.append(stemmed_tokens)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=nb_sujets, id2word = dictionary, passes=20)
    print(ldamodel.print_topics(num_topics=3, num_words=3))
    
    
#def telecharger_onto(lien):
 #   onto_path.append("C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\")
  #  onto.load()
   # return onto

    
#-*- coding: utf-8 -*-

"""

@file

@brief Various function to download data about population

"""

import re

from pyquickhelper.loghelper import noLOG

from pymyinstall.installcustom import download_page

from pyensae import download_data

from pyrsslocal.xmlhelper import xml_filter_iterator

#from .data_exceptions import LinkNotFoundError





def wolf_xml(url="http://alpage.inria.fr/~sagot/wolf.html", temp_folder=".", fLOG=noLOG):

    """

    The `WOLF <http://alpage.inria.fr/~sagot/wolf-en.html>`_

    (Wordnet Libre du Fran�ais, Free French Wordnet) is a free semantic lexical resource (wordnet) for French.



    This data is licensed under

    `Cecill-C license <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>`_.

    Language is French.



    @param      url             url

    @param      fLOG            logging function

    @param      temp_folder     where to download

    @return                     list of files

    """

    link = url

    page = download_page(link)

    reg = re.compile("href=\\\"(.*wolf.*?[.]bz2)\\\"")

    alls = reg.findall(page)

    if len(alls) == 0:

        raise LinkNotFoundError(

            "unable to find a link on a .exe file on page: " +

            page)



    url = alls[0]

    spl = url.split("/")

    url = "/".join(spl[:-1]) + "/"

    url2 = "/".join(spl[:-2]) + "/31718/"

    name = spl[-1]

    dtd = download_data("debvisdic-strict.dtd", url=url2,

                        fLOG=fLOG, whereTo=temp_folder)

    local = download_data(name, url=url, fLOG=fLOG, whereTo=temp_folder)

    if isinstance(local, str):

        local = [local]

    return local + [dtd]





def enumerate_wolf_xml_row(filename, fLOG=noLOG, xmlformat=False, encoding="utf-8"):

    """

    walk through an XML file returned by function

    @see fn wolf_xml



    @param      filename        filename

    @param      fLOG            logging function

    @param      xmlformat       if True, return the xml, otherwise return the node,

                                see `XMLHandlerDictNode <http://www.xavierdupre.fr/app/pyrsslocal/helpsphinx//pyrsslocal/xmlhelper/xml_tree_node.html#module-pyrsslocal.xmlhelper.xml_tree_node>`_

    @param      encoding        encoding

    @return                     elements

    """

    for row in xml_filter_iterator(filename, xmlformat=xmlformat, fLOG=fLOG, encoding=encoding):

        yield row




filename='C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\wolf-1.0b4.xml'
def enumerate_wolf_synonyms(filename,mot, fLOG=noLOG, encoding="utf-8"):

    """

    enumerate list of synonyms

    Language is French.



    @param      filename        xml file

    @param      fLOG            logging function

    @param      encoding        encoding

    @return                     iterator on list of words

    """

    for row in enumerate_wolf_xml_row(filename, fLOG=fLOG, encoding=encoding):
        syn = [v for k, v in row.iterfields() if k == "SYNSET/SYNONYM/LITERAL/_"]
        if (mot in syn and len(syn)>1):

            yield(syn)


def analyse_sujet(question):
    mot_cle=[]
    for i in programme_freq(question)[0]:
        count=0
        longueur=0
        if i not in mot_cle:
            for synset in enumerate_wolf_synonyms('C:\\Users\\Paul\\Documents\\ecole\\info\\projetS2\\verbatim\\code\\code_py\\wolf-1.0b4.xml',i):
                longueur=longueur+len(synset)
                for mot in synset:
                    if mot not in mot_cle:
                        count=count+1
            if (count==longueur):
                mot_cle.append(i)
    return mot_cle