#Board games (CREATE)
#Recommend and find board games for the user

import pandas as pd
import random

#This dataset is taken from: https://docs.google.com/spreadsheets/d/19HV_7dWZzXpFsvVQXToTl2SrWT-uqio8oPxGTzameq8/edit?gid=0#gid=0
data = pd.read_csv('Boardgames.csv')

name = data['Name'].tolist()
max_player = data['Maximum players'].tolist()
min_player = data['Minimum players'].tolist()
category = data['Category'].tolist()
mechanics = data['Mechanics'].tolist()
game_time = data['Average game time'].tolist()
game = []


def genre(): #Written by me
    cate = input("What kind of category do you want to play? (adventure, fantasy, economic, or action): ") 
    if cate == "adventure": #Depending on what the user inputs, the computer recommends a random game on each category
        for i in range(len(name)):
            if "Adventure" in category[i]:
                game.append(name[i])
        rec = random.randint(0, len(game))
        print(f"You are recommended: {game[rec]}")
        game.clear()
    elif cate == "fantasy":
        for i in range(len(name)):
            if "Fantasy" in category[i]:
                game.append(name[i])
        rec1 = random.randint(0, len(game))
        print(f"You are recommended: {game[rec1]}")
        game.clear()
    elif cate == "economic":
        for i in range(len(name)):
            if "Economic" in category[i]:
                game.append(name[i])
        rec2 = random.randint(0, len(game))
        print(f"You are recommended: {game[rec2]}")
        game.clear()
    else:
        for i in range(len(name)):
            if "Action" in category[i]:
                game.append(name[i])
        rec3 = random.randint(0, len(game))
        print(f"You are recommended: {game[rec3]}")
        game.clear()

def mech(type):
    number = 0
    for i in range(len(name)):
        if type in mechanics[i]:
            game.append(name[i])
            number = number + 1
    if number > 0:
        rec4 = random.randint(0, len(game))
        print(f"You are recommended: {game[rec4]}")
        game.clear()
    else:
        print("There is no matching game.")

def gametime(): #A board game is randomly generated based on the player's inputted game time in minutes. --- Written by partner
    time = int(input("What is your preferred game time? (max 1000 minutes, multiples of 5's): "))
    for i in range(len(game_time)):
        if game_time[i] == time:
            game.append(name[i])
    reco = random.randint (0, len(game))
    print(f"You are recommended: {game[reco]}")
    game.clear()

def group(): #A board game is randomly generated based on the player's inputted group size. ---- Written by partner
    size = input("What is your group size? (small, medium, large): ")
    if size == "small":
        for i in range(len(name)):
            if max_player[i] <= 4:
                game.append(name[i])
        reco1 = random.randint(0, len(game))
        print(f"You are recommended: {game[reco1]}")
        game.clear()
    elif size == "medium":
        for i in range(len(name)):
            if max_player[i] <= 10:
                game.append(name[i])
        reco2 = random.randint(0, len(game))
        print(f"You are recommended: {game[reco2]}")
        game.clear()
    else:
        for i in range(len(name)):
            if max_player[i] <= 20:
                game.append(name[i])
        reco1 = random.randint(0, len(game))
        print(f"You are recommended: {game[reco1]}")
        game.clear()


def menu():
    while True:
        print("---------------------------------------------------------------------------------------------------------")
        play = input("Do you want to find a board game based on the category, mechanic, group size, time, or quit?: ")
        if play == "category":
            genre()
        elif play == "mechanic":
            mech1 = input("What type of mechanic do you want to look up?: ")
            mech(mech1)
        elif play == "group size":
            group()
        elif play == "time":
            gametime()
        else:
            break

menu()
