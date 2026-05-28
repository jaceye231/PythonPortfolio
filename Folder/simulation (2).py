#Jacey
#Simulation
#🐢 The Tortoise
#🐇 The Hare

import random

finish_line = 50
tortoise_pos = 0
hare_pos = 0
is_hare_asleep = False
tortoise_wins = 0
hare_wins = 0

for i in range(100000):
    while tortoise_pos < finish_line and hare_pos < finish_line:
        rand_tor = random.randint(1, 3)
        tortoise_pos = tortoise_pos + rand_tor
        rand_sleep = random.randint(1, 100)
        if rand_sleep <= 98:
            is_hare_asleep = True
        else:
            is_hare_asleep = False
        if is_hare_asleep == False:
            rand_hare = random.randint(1, 10)
            hare_pos = hare_pos + rand_hare

    if tortoise_pos >= finish_line:
        tortoise_wins = tortoise_wins + 1
        tortoise_pos = 0
    else:
        hare_wins = hare_wins + 1
        hare_pos = 0

print(f"Tortoise Wins: {tortoise_wins} | Hare Wins: {hare_wins}")
