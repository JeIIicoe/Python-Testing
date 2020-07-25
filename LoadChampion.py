import requests
import json
import urllib
from Champion import *

champ_list = list()

def load_champion_file(): #Loads championjson.json & returns it
    with open('files/champion.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
        return json_data

champ_data = load_champion_file()

if champ_data is not None:
    for k, v in champ_data['data'].items():
        champ_list.append(Champion(v['key'], v['name'],v['title']))

def all_champs(): #Print every champ name, title & key
    for Champion in champ_list :
        print(f'{Champion.return_name():16} - {Champion.return_title():34} | Key: {Champion.return_key()}')

def one_champ(): #finds one champion
    for Champion in champ_list :
        if Champion.return_name() == name :
           print(f'{Champion.return_name():16} - {Champion.return_title():34} | Key: {Champion.return_key()}')

name = urllib.parse.quote(input("\nChamp Name: "))
one_champ()