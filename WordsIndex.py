from ast import Global
import random

from unicodedata import category

#make a list of the ranks and suits
#Food = []
#Object = []
Place = ["Missouri" ,"Rome" , "Paris" , "Italy" , "DC", "Egypt"]
Animal = ["Cat", "Dog", "Horse","Pig","Sheep","Wolf","goat"]
Global_Artist = ["Green Day","Bad Bunny","Taylor Swift","Katseye", "Black Pink"]

category = ["Place", "Animal", "Global_Artist"]
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
randAnimal = random.randint(0,6)
randArtist = random.randint(0,4)

print(f"The Category is: {randCat}")

if randCat == 0:
    print(f"The word is:  {Place[randPlace]} ")
elif randCat == 1:
    print(f"The word is:  {Animal[randAnimal]} ")
elif randCat == 2:
    print(f"The word is:  {Global_Artist[randArtist]} ")








