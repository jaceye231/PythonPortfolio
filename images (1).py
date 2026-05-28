#Jacey
#Images
#Tutorial on how to open images using python

import webbrowser

url = ["https://tinyurl.com/4r2zwedh","https://tinyurl.com/2zpxww9r","https://tinyurl.com/yd2x822z","https://tinyurl.com/3v5ssav7"]
descriptions = ["I recommend going with family and friends.", "I recommend trying the food.", "I recommend trying everything out and exploring everything.", "I recommend bringing neccessary supplies when exploring outdoors."]
#webbrowser.open(url)

def vacation():
    climate = input("Do you prefer a hot or cold climate? (hot or cold): ")
    if climate == "hot":
        outside = input("Would you like to explore outdoors or within the city?(outdoors or city): ")
        if outside == "outdoors":
            webbrowser.open(url[1])
            print("In the Caribbean, there are a variety of beaches, adventure tours, hiking, and local places. There are many activites such as snorkeling, diving, whale watching, and more.")
            print(descriptions[0])
        else:
            webbrowser.open(url[2])
            print("Spain offers a blend of art and architecture along with its vibrant culture. There are many iconic landmarks and festivals to visit.")
            print(descriptions[2])
    else:
        outside1 = input("Would you like to explore outdoors or within the city?(outdoors or city): ")
        if outside1 == "outdoors":
            webbrowser.open(url[0])
            print("Alaska offers incredible adventures including national parks, wildlife watching, northern lights, fishing, etc. They also have museums on native culture and Gold Rush History.")
            print(descriptions[3])
        else:
            webbrowser.open(url[3])
            print("Denmark offers stunning gardens, historical sites, museums, amusement parks, and castles. There are activites such as sailing, ice skating, and eating New Nordic cuisine.")
            print(descriptions[1])

vacation()


#Sources of Information
#Alaska:
#URL: https://explorewithalec.com/best-time-to-visit-alaska/
#Title: Ultimate Guide: Find out the Best Time to Visit Alaska
#Author Name: Alec Sills-Trausch
#Date: January 24, 2023

#Denmark:
#URL: https://travel.com/regions/europe/denmark/denmark-best-things-to-do-top-picks/
#Title: Denmark: Best Things To Do - Top Picks

#Spain:
#URL: https://www.islands.com/1899745/best-places-where-stay-barcelona-spain/
#Title: The Best Places To Stay In Barcelona Based On What You Want From The Trip, According To Reviews
#Author: Berry Peacock
#Date: July 7, 2025

#Caribbean:
#URL: https://aerialbvi.com/blog/caribbean-weather-guide/
#Title: Weather in the Caribbean: A Guide for Future Visitors
#Author: Britnie Turner
#Date: April 9, 2024
