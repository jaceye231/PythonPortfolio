#Jacey
#Hacker

import pandas as pd

data = pd.read_csv('hacker.csv')

log_id = data['Log_ID'].tolist()
ip_address = data['IP_Address'].tolist()
protocol = data['Protocol'].tolist()
data_kb = data['Data_KB'].tolist()
time = data['Time'].tolist()
description = data['Description'].tolist()
login = []

def failed():
    for i in range(len(time)):
        if "Failed" in description[i]:
            print([i])

def stole():
    for i in range(len(time)):
        if data_kb[i] > 2000:
            print([i])

def reset():
    for i in range(len(time)):
        if "Force" in description[i]:
            login.append(log_id[i])
    print(f"Total accounts that force password reset: {len(login)}")

#failed()
print(data.loc[[196]])
#stole()
print(data.loc[[199]])
reset()
