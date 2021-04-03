# -*- coding: utf-8 -*-

from functions import *

def main():
    #La génération des paramètres du générateur de pommes
    ptot=0 #le dénominateur, somme des 3 probabilités
    mu=[0,0,0] #les 3 moyennes, entre 0 et 10
    sigma=[0,0,0] #les 3 écarts types entre 0 et 10
    p=[0,0,0] #la probabilité de chaque arbre

    for i in range(3):
      mu[i]=random.random()*10
      sigma[i]=random.random()*10
      p[i]=random.random()
      ptot+=p[i]

    for i in range(3):
      p[i]=p[i]/ptot

    #Affichage
    for i in range(3):
      print(mu[i],sigma[i],p[i])


    #On teste
    #for i in range(10):
    #  generepomme(mu,sigma,p)

    #Protocole de test de la solution
    nb_tests=0
    nb_corrects=0
    tirages=[]

    for i in range(3600):
      x,y=baseline(tirages,nb_tests)#ici remplacer baseline par le nom de la fonction à tester
      #x,y=dernier_vu(tirages,nb_tests)

      z=generepomme(mu,sigma,p)
      #print('x',x,'y',y,'z',z, nb_corrects,nb_tests)
      tirages.append(z)

      if abs(x-z)<0.5 or abs(y-z)<0.5: #diamètre du seau=1, donc rayon=0.5
        nb_corrects+=1
      nb_tests+=1

    print('Nombre de pommes ramassées, sur 100 tombées :',100*nb_corrects/nb_tests)


main()
