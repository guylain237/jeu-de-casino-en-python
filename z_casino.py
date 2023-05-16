import os
import pickle
from random import randrange
from math import *
r=os.getcwd()
print(r)
monargent = 1000
name = input("nom du joueur : ")

print("bienvenue dans la partie monsieur ",name ,"vous disposez de ",monargent," $ pour participer au jeu de casino" )
while 1:
    nbre_mise = -1
    min = 0
    max = 49
    while nbre_mise < min or nbre_mise > max:
         nbre_mise = int(input("veuillez entrez un nombre compris entre 0 et 49 mr : "))
         nbre_mise = int(nbre_mise)
         with open("score","wb") as fichier:
             pickle.Pickler(fichier).dump(nbre_mise)
         with open("score", "rb") as fichier:
             pickle.Unpickler(fichier).load()
         print(" vous avez choisir le numero ", nbre_mise)
    mise = -1
    while mise < 0 or mise > monargent:
        mise =input("mr  combien voulez vous misez pour cette partie :")
        mise = int(mise)
        with open("score","wb") as fichier:
            pickle.Pickler(fichier).dump(mise)
    numero_gagnant = randrange(50)
    print("beep....beep....beep...beep...beep...beep on a le numero : ",numero_gagnant)
    if numero_gagnant == nbre_mise :
         print("bravo monsieur ", name ," vous venez de remporter la somme de ",mise*3 ," $ avec votre mise de ",mise)
         monargent+=mise
         with open("score","wb") as fichier:
             pickle.Pickler(fichier).dump(monargent)
         print("votre solde actuelle est ", monargent)
    elif numero_gagnant % 2 == nbre_mise % 2:
         print("votre nombre est pair vous aurez la moitie de votre mise ", name)
         monargent -=mise
         mise = ceil(mise*0.5)
         monargent += mise
         with open("score","wb") as fichier:
             pickle.Pickler(fichier).dump(monargent)
         print("votre nouveau solde est de ", monargent)
    else:
         print("c est pas votre tour de chance veuillez reessayer mr ", name)
         monargent -= mise
         with open("score","wb") as fichier:
             pickle.Pickler(fichier).dump(monargent)
         print("il vous reste , ", monargent, " $ dans votre solde reflechissez bien avant de continuer le jeu mr ", name)
    if monargent <= 0:
        print("vous avez perdu tout votre argent mr ", name, " aurevoir! ")
        with open("score","wb") as fichier:
            pickle.Pickler(fichier).dump(monargent)
        break
    else:
       print("votre nouveau solde est : ",monargent)
       with open("score","wb") as fichier:
           pickle.Pickler(fichier).dump(monargent)
       quitter = input("souhaitez vous continuer la partie mr ")
       if quitter == "o" or quitter == "O":
           print("votre solde est de : ",monargent )
       if quitter.lower()=="n":
           break
os.chdir("c:\\casino")
f=os.getcwd()
print(f)

os.system("pause")




