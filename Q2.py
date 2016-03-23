#!/usr/bin/python3

'''
    Cricket Score Notifier
------------------------------------------------------------
Script written in python3

OS : Ubuntu 

To run use :
python3 Q2.py
-------------------------------------------------------------
External modules:
sudo pip3 install notify2
---------------------------------------------------------------
Note:
1.After every 2 minutes score,team and time will be displayed
  on top-right corner as notification using notify2 module

2.Scores will be saved in file "cricket_score.txt"
---------------------------------------------------------------------
Author : 
Prashant Kumar - KF09550
Pradeep kumar - KF05049
Team Id 	  - TK097042 

_______________________________________________________________
'''



import requests
import json
import pprint
import time
from datetime import datetime
import notify2
notify2.init('Cricket Notifier')
print("Initialising...")
base_url = "http://crm.wherrelz.com/api/cricketScore/?unique_id="
count=0
while count<3:
    try:
        r = requests.get("http://crm.wherrelz.com/api/cricket/")
        break
    except:
        count+=1
if count==3:
    print("Network Error")
    exit()

all_match1 = json.loads(r.text)
all_match = all_match1['data']
print("Choose from following ongoing matches : ")
k=0
for i in all_match:
    print(str(k)+". "+i['description'])
    k+=1

choice = int(input())
match_id = all_match[choice]['unique_id']
url = base_url + str(match_id)
count=0
print(url)
with open('cricket_score.txt', 'w') as f:
    while True:
        rMatch = requests.get(url)
        match_desc = json.loads(rMatch.text)
        print("################## Score ########################")
        score = match_desc['score']
        t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(score+" "+t)
        n = notify2.Notification("Score",score+" time: "+t)
        f.write(score+" Time : "+t+"\n")
        n.show()
        print("Next Score After 2 minutes... ")
        time.sleep(120)
