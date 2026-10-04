import os
import random

from ast import Global
import random

from unicodedata import category

PLACE = ["Missouri" ,"Rome" , "Paris" , "Italy" , "DC", "Egypt"]
PHINTS = ["Show me", "Ceaser", "Tower", "Boot", "President", "Desert"]

ANIMAL = ["Cat", "Dog", "Horse","Pig","Sheep","Wolf","goat"]
AHINTS = ["Claws", "Loyal","Ride", "Mud", "Flock", "Loner", "Mountain"]

ARTIST = ["Green Day","Bad Bunny","Taylor Swift","Katseye", "Black Pink"]
ARTHINTS = ["American Idiot", "Superbowl", "Eras","WILDWORD", "YG Entertainment"]

CATEGORY = ["Place", "Animal", "Global_Artist"]

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
        return f"The word is:  {PLACE[randPlace]} "



    elif randCat == 1:
        print(f"The word is:  {ANIMAL[randAnimal]} ")
        return f"The word is:  {ANIMAL[randAnimal]} "
        print(f"The hint is: {AHINTS[randAnimalHint]} ")

    elif randCat == 2:
        return f"The word is:  {ARTIST[randArtist]} "
        print(f"The hint is: {ARTHINTS[randArtistHint]} ")

def hint():
    if randCat == 0:
        print(f"The hint is: {PHINTS[randAnimal]} ")
        return f"The hint is: {PHINTS[randPlaceHint]} "



    elif randCat == 1:
        print(f"The hint is: {ANIMAL[randAnimal]} ")
        return f"The hint is: {AHINTS[randAnimalHint]} "

    elif randCat == 2:
        print(f"The hint is: {ARTIST[randArtist]} ")
        return f"The hint is: {ARTHINTS[randArtistHint]} "


num_players = int(input("Enter number of players: "))

if num_players > 1:
    player1 = (input("enter your name: "))
    print(player1)
else:
        print("Invalid number")
if (num_players > 2) or (num_players == 2):
    player2 = (input("Enter your name: "))
    print(player2)
if (num_players > 3) or (num_players == 3):
    player3 = (input("Enter your name: "))
    print(player3)
if (num_players > 4) or (num_players == 4):
    player4 = (input("Enter your name: "))
    print(player4)
if (num_players > 5) or (num_players == 5):
    player5 = (input("Enter your name: "))
    print(player5)
if (num_players > 6) or (num_players == 6):
    player6 = (input("Enter your name: "))
    print(player6)
if (num_players > 7) or (num_players == 7):
    print("Too many players")

wolf = random.randint(1, num_players)

def RoleAssign():
    if wolf == 1:
        confirm = input(f"{player1}, Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is", hint())
            os.system("cls")
    else:
        confirm = input(f"{player1}, Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are a sheep. The word is", word())
            os.system("cls")



RoleAssign()







"""
for i in range(0, players):
    player = (input("Enter your name: "))
    print(player)
"""