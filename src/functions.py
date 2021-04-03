#Les importations
import numpy as np
import random
import matplotlib.pyplot as plt

def printGaussienne():
    #Un bout de code pour représenter graphiquement une gaussienne
    mu = 0
    sigma=1
    nums=[]
    for i in range(10000):
        temp = random.gauss(mu, sigma)
        nums.append(temp)

    # plotting a graph
    plt.hist(nums, bins = 200)
    plt.show()


#Le générateur de pommes
def generepomme(mu,sigma,p):
  r=random.random()

  if r<p[0]:
    arbre=0

  elif r<p[0]+p[1]:
    arbre=1

  else: arbre=2 #on a sélectionné l'arbre

  pos=random.gauss(mu[arbre], sigma[arbre]) #on applique l'arbre
  #print(arbre,pos)
  return pos

def baseline(tirages,nbtests):
  return(random.random()*5,5+random.random()*5)
  #cet algorithme est stupide et fonctionne assez mal! Dans ce cas il n'y a pas de paramètre mais on peut utiliser en particulier l'historique des pommes précédentes !

def dernier_vu(tirages,nb_tests):#une heuristique: mettre le panier là où la dernière pomme est tombée
  if nb_tests>1:
    xx=tirages[nb_tests-1]
    yy=tirages[nb_tests-2]
  elif nb_tests>0:
    xx=tirages[nb_tests-1]
    yy=0.3
  else:
    xx=0.7
    yy=0.3
  return(x,y)

def tache1(tirages,nb_tests):
    pass

def tache2(tirages,nb_tests):
    pass

def tache3(tirages,nb_tests):
    pass
