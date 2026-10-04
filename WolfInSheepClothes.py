import os
import random

from WordsIndex import *

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

imposter = random.randint(1, num_players)

def RoleAssign():
    if imposter == 1:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is",{hint})
            os.system("cls")
    else:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print(f"you are a sheep. The word is",{word})
            os.system("cls")

    if imposter == 2:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is",{hint})
            os.system("cls")
    else:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print(f"you are a sheep. The word is",{word})
            os.system("cls")

    if imposter == 3:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is",{hint})
            os.system("cls")
    else:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print(f"you are a sheep. The word is",{word})
            os.system("cls")

    if imposter == 4:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is",{hint})
            os.system("cls")
    else:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print(f"you are a sheep. The word is",{word})
            os.system("cls")

    if imposter == 5:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is", {hint})
            os.system("cls")
    else:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print(f"you are a sheep. The word is", {word})
            os.system("cls")

    if imposter == 6:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print("you are the wolf. Your hint is",{hint})
            os.system("cls")
    else:
        confirm = input("Do you wish to view your role? (y/n): ")
        if confirm == "y":
            print(f"you are a sheep. The word is",{word})
            os.system("cls")

RoleAssign()







"""
for i in range(0, players):
    player = (input("Enter your name: "))
    print(player)
"""