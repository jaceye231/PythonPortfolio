#Jacey
#Dog Breed
#The purpose of my program is to help users choose a dog breed that meets their needs

#Init
import pandas as pd
import webbrowser
import random

data = pd.read_csv('dog.csv')

name = data['Name'].tolist()
max_weight = data['Maximum Weight'].tolist()
min_weight = data['Minimum Weight'].tolist()
temperament = data['Temperament'].tolist()
image = data['Image'].tolist()
bredfor = data['BredFor'].tolist()
dogs = []

#Functions
def dogsize():
    size = input("What dog size do you prefer? (tiny, small, medium, or large): ")
    if size == "tiny":
        for i in range(len(name)):
            if max_weight[i] <= 10:
                dogs.append(name[i])
        rec = random.randint(0, len(dogs))
        print(f"I recommend this dog: {dogs[rec]}")
        print(f"If you don't like that dog, here is a list of tiny dogs: {dogs}")
        dogs.clear()
    elif size == "small":
        for i in range(len(name)):
            if max_weight[i] <= 25 and min_weight[i] >= 11:
                dogs.append(name[i])
        rec1 = random.randint(0, len(dogs))
        print(f"I recommend this dog: {dogs[rec1]}")
        print(f"If you don't like that dog, here is a list of small dogs: {dogs}")
        dogs.clear()
    elif size == "medium":
        for i in range(len(name)):
            if max_weight[i] <= 60 and min_weight >= 26:
                dogs.append(name[i])
        rec2 = random.randint(0, len(dogs))
        print(f"I recommend this dog: {dogs[rec2]}")
        print(f"If you don't like that dog, here is a list of medium dogs: {dogs}")
        dogs.clear()
    else:
        for i in range(len(name)):
            if max_weight[i] > 60:
                dogs.append(name[i])
        rec3 = random.randint(0, len(dogs))
        print(f"I recommend this dog: {dogs[rec3]}")
        print(f"If you don't like that dog, here is a list of large dogs: {dogs}")
        dogs.clear()

def temp(breed_name):
    number = 0
    for i in range(len(name)):
        if breed_name in name[i]:
            print(temperament[i])
            webbrowser.open(image[i])
            number = number + 1
    if number == 0:
            print("Sorry, your dog isn't on the list")

def breed(purpose):
    num = 0
    for i in range(len(name)):
        if purpose in bredfor[i]:
            dogs.append(name[i])
            num = num + 1
    rec4 = random.randint(0, len(dogs))
    print(f"I recommend this dog: {dogs[rec4]}")
    print(f"Here are all the other dogs that matches your input: {dogs}")
    dogs.clear()
    if num == 0:
        print("There are no matching breeds")

def menu():
    while True:
        interface = input("Do you want to find a dog based on size (size), find a dog's temperament (temperament), look for a dog with a specfic trait (trait), or quit?: ")
        if interface == "size":
            dogsize()
        elif interface == "temperament":
            temp1 = input("What dog do you want to look up?: ")
            temp(temp1)
        elif interface == "trait":
            trait = input("What dog trait do you want to look up?: ")
            breed(trait)
        else:
            break

#Main
menu()

#Sources
#Mr. J shared this data with me
