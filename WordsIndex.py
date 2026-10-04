from ast import Global
import random

from unicodedata import category

#make a list of the ranks and suits
#Food = []
#Object = []
PLACE = ["Missouri" ,"Rome" , "Paris" , "Italy" , "DC", "Egypt"]
PHINTS = ["Show me", "Ceaser", "Tower", "Boot", "President", "Desert"]

ANIMAL = ["Cat", "Dog", "Horse","Pig","Sheep","Wolf","goat"]
AHINTS = ["Claws", "Loyal","Ride", "Mud", "Flock", "Loner", "Mountain"]

ARTIST = ["Green Day","Bad Bunny","Taylor Swift","Katseye", "Black Pink"]
ARTHINTS = ["American Idiot", "Superbowl", "Eras","WILDWORD", "YG Entertainment"]

CATEGORY = ["Place", "Animal", "Global_Artist"]
#Hint = []

#pick a random rank and suit
"""
randRank = random.randint(0,12)
randSuit = random.randint(0,4)
"""
#print(f"The card you picked is {rank[randRank]} of {suit[randSuit]}")
#print(random.choice((Category))) # Print random word





randCat = random.randint(0,2)

randPlace = random.randint(0,5)
randPlaceHint = randPlace

randAnimal = random.randint(0,6)
randAnimalHint = randAnimal

randArtist = random.randint(0,4)
randArtistHint = randArtist

print(f"The Category is: {CATEGORY[randCat]}")

def word():
    if randCat == 0:
        print(f"The word is:  {PLACE[randPlace]} ")
        print(f"The hint is: {PHINTS[randPlaceHint]} ")



    elif randCat == 1:
        print(f"The word is:  {ANIMAL[randAnimal]} ")
        print(f"The hint is: {AHINTS[randAnimalHint]} ")

    elif randCat == 2:
        print(f"The word is:  {ARTIST[randArtist]} ")
        print(f"The hint is: {ARTHINTS[randArtistHint]} ")

def hint():
    if randCat == 0:
        print(f"The hint is: {PHINTS[randPlaceHint]} ")



    elif randCat == 1:
        print(f"The hint is: {AHINTS[randAnimalHint]} ")

    elif randCat == 2:
        print(f"The hint is: {ARTHINTS[randArtistHint]} ")











