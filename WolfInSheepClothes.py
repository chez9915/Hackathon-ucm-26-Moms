import os
import random

from ast import Global
import random
from PIL import Image
from unicodedata import category
im = Image.open("C:/Users/Aiden/Downloads/wolf_in_sheep.jpg")
im.show()
PLACE = ["Missouri" ,"Rome" , "Paris" , "Italy" , "DC", "Egypt"]
PHINTS = ["Show me", "Ceaser", "Tower", "Boot", "President", "Desert"]

ANIMAL = ["Cat", "Dog", "Horse","Pig","Sheep","Wolf","goat"]
AHINTS = ["Claws", "Loyal","Ride", "Mud", "Flock", "Loner", "Mountain"]

ARTIST = ["Green Day","Bad Bunny","Taylor Swift","Katseye", "Black Pink"]
ARTHINTS = ["American Idiot", "Superbowl", "Eras","WILDWORD", "YG Entertainment"]

FOOD = ["Mac and Cheese", "Burger", "Pizza", "Cookies"]
FHINTS = ["Noodle", "Beef", "Pizza", "Baked"]

OBJECTS = ["Hair Brush", "Boots", "Book", "Castle"]
OHINTS = ["Detangle", "Cowboy", "Page", "Royalty"]

CATEGORY = ["Place", "Animal", "Global_Artist", "Food", "Object"]

randCat = random.randint(0,4)

randPlace = random.randint(0,5)
randPlaceHint = randPlace

randAnimal = random.randint(0,6)
randAnimalHint = randAnimal

randArtist = random.randint(0,4)
randArtistHint = randArtist

randFood = random.randint(0,3)
randFoodHint = randFood

randObject = random.randint(0,3)
randObjectHint = randObject


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

    elif randCat == 3:
        return f"The word is:  {FOOD[randFood]} "
        print(f"The hint is: {FHINTS[randFoodHint]} ")

    elif randCat == 4:
        return f"The word is:  {OBJECTS[randObject]} "
        print(f"The hint is: {OHINTS[randObjectHint]} ")

def hint():
    if randCat == 0:
        print(f"The word is: {PLACE[randPlace]} ")
        return f"The hint is: {PHINTS[randPlaceHint]} "



    elif randCat == 1:
        print(f"The word is: {ANIMAL[randAnimal]} ")
        return f"The hint is: {AHINTS[randAnimalHint]} "

    elif randCat == 2:
        print(f"The word is: {ARTIST[randArtist]} ")
        return f"The hint is: {ARTHINTS[randArtistHint]} "

    elif randCat == 3:
        print(f"The word is: {FOOD[randFood]} ")
        return f"The hint is: {FHINTS[randFoodHint]} "

    elif randCat == 4:
        print(f"The word is: {OBJECTS[randObject]} ")
        return f"The hint is: {OHINTS[randObjectHint]} "


num_players = int(input("Enter number of players: "))

if num_players > 1:
    player1 = (input("enter your name: "))
    #print(player1)
else:
        print("Invalid number")
if (num_players > 2) or (num_players == 2):
    player2 = (input("Enter your name: "))
    #print(player2)
if (num_players > 3) or (num_players == 3):
    player3 = (input("Enter your name: "))
    #print(player3)
if (num_players > 4) or (num_players == 4):
    player4 = (input("Enter your name: "))
    #print(player4)
if (num_players > 5) or (num_players == 5):
    player5 = (input("Enter your name: "))
    #print(player5)
if (num_players > 6) or (num_players == 6):
    player6 = (input("Enter your name: "))
    #print(player6)
if (num_players > 7) or (num_players == 7):
    print("Too many players")

wolf = random.randint(1, num_players)

#print(wolf)

if wolf == 1:
    confirm1 = input(f"{player1} Do you wish to view your role? (y/n): ")
    if confirm1 == "y":
        print(f"{player1} you are the wolf. ", hint())
if wolf != 1:
    confirm1 = input(f"{player1} Do you wish to view your role? (y/n): ")
    if confirm1 == "y":
        print(f"{player1} you are a sheep. The word is", word())
viewed1 = input("Have you seen you role? y/n")
if viewed1 == "y":
    print("\n"*100)
if wolf == 2:
    confirm2 = input(f"{player2} Do you wish to view your role? (y/n): ")
    if confirm2 == "y":
        print(f"you are the wolf. ", hint())
if wolf != 2:
    confirm2 = input(f"{player2} Do you wish to view your role? (y/n): ")
    if confirm2 == "y":
        print(f"{player2} you are a sheep. The word is", word())
viewed2 = input("Have you seen you role? y/n: ")
if viewed2 == "y":
    print("\n"*100)
if wolf == 3:
    confirm3 = input(f"{player3} Do you wish to view your role? (y/n): ")
    if confirm3 == "y":
        print(f"you are the wolf. ", hint())
if wolf != 3:
    confirm3 = input(f"{player3} Do you wish to view your role? (y/n): ")
    if confirm3 == "y":
        print(f"{player3} you are a sheep. The word is", word())
viewed3 = input("Have you seen you role? y/n: ")
if viewed3 == "y":
    print("\n"*100)
if wolf == 4:
    confirm4 = input(f"{player4} Do you wish to view your role? (y/n): ")
    if confirm4 == "y":
        print(f"you are the wolf. ", hint())
if wolf != 4:
    confirm4 = input(f"{player4} Do you wish to view your role? (y/n): ")
    if confirm4 == "y":
        print(f"{player4} you are a sheep. The word is", word())
viewed4 = input("Have you seen you role? y/n: ")
if viewed4 == "y":
    print("\n"*100)




"""
for i in range(0, players):
    player = (input("Enter your name: "))
    print(player)
"""


"""

def WolfAssign():
    if wolf == 1:
        confirm = input(f"{player1}, Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is", hint())
            print("\n"*100)
    elif wolf == 2:
        confirm = input(f"{player2}, Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is", hint())
            print("\n"*100)
    elif wolf == 3:
        confirm = input(f"{player3}, Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is", hint())
            print("\n"*100)
    elif wolf == 4:
        confirm = input(f"{player4}, Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is", hint())
            print("\n"*100)
    elif wolf == 5:
        confirm = input(f"{player5}, Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is", hint())
            print("\n"*100)
    elif wolf == 6:
        confirm = input(f"{player6}, Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is", hint())
            print("\n"*100)

def SheepAssign():
    if wolf != player1:
      player1Answer = print(input(f"{player1},Are you ready to view your role? (y/n): "))
    if player1Answer == "y":
        print("You are a sheep the word is , word())")

    if wolf != player2:
      player2Answer = print(input(f"{player2},Are you ready to view your role? (y/n): "))
    if player2Answer == "y":
        print("You are a sheep the word is , word())")
        print("\n" * 100)
    if wolf != player3:
      player3Answer = print(input(f"{player3},Are you ready to view your role? (y/n): "))
    if player3Answer == "y":
        print("You are a sheep the word is , word())")
        print("\n" * 100)
    if wolf != player4:
      player4Answer = print(input(f"{player4},Are you ready to view your role? (y/n): "))
    if player4Answer == "y":
        print("You are a sheep the word is , word())")
        print("\n" * 100)
    if wolf != player5:
      player5Answer = print(input(f"{player5},Are you ready to view your role? (y/n): "))
    if player5Answer == "y":
        print("You are a sheep the word is , word())")
        print("\n" * 100)
    if wolf != player6:
      player6Answer = print(input(f"{player6},Are you ready to view your role? (y/n): "))
    if player6Answer == "y":
        print("You are a sheep the word is , word())")
        print("\n" * 100)

"""