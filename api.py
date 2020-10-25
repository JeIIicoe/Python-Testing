import requests
import json
import urllib
from datetime import datetime, timezone
from Champion import *
from MatchHistory import *

api_token = 'xxxxxx'
api_url_base = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
api_mastery_url_base = 'https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'
api_ranked_url_base = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'

champ_list = list()

def get_account_info(): #Gets an Account from the Summoner Name

    response_string = api_url_base + name + '?api_key=' + api_token
    response = requests.get(response_string)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None



def load_champion_file(): #Loads championjson.json & returns it
    with open('files/champion.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
        return json_data



def get_account_mastery(summ_id): #Gets an account's chamption mastery json list from an AccountID
    response_string = api_mastery_url_base + summ_id + '?api_key=' + api_token
    response = requests.get(response_string)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None



def get_account_rank(summ_id): #Gets an account's ranked stats from an AccountID
    response_string = api_ranked_url_base + summ_id + '?api_key=' + api_token
    response = requests.get(response_string)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8')) 
    else: 
        return None 

def winLossRatio(wins, losses): #Calculates win/loss % ratio
    ratio = (wins / (wins + losses)) * 100 #wrong
    return round(ratio, 2)

def GoThroughHistory(start, end):
    for i in range(start, end) :
        champ_id = match_list[i]['champion']
        timestamp = int(match_list[i]['timestamp'])
        timedate = datetime.fromtimestamp(timestamp // 1000)
        for Champion in champ_list :
            if champ_id == int(Champion.return_key()) :
                print('You played', Champion.return_name(), 'at', timedate)


#Everything starts here
champ_data = load_champion_file()

if champ_data is not None:
    for k, v in champ_data['data'].items():
        champ_list.append(Champion(v['key'], v['name'],v['title']))

else:
    print(':(')

name = urllib.parse.quote(input("\nSummoner Name: "))

account_info = get_account_info()

if account_info is not None:

    summ_id = account_info['id']
    acc_id = account_info['accountId']
    acc_level = account_info['summonerLevel']
    acc_icon = account_info['profileIconId']
    acc_name = account_info['name']

    ranked_info = get_account_rank(summ_id)
    mastery_info = get_account_mastery(summ_id)
    TotalMatchList = get_match_list(acc_id, api_token)
    match_list = TotalMatchList['matches']

    print("-------------------------------------------")
    print("\nSUMMONER: ", acc_name, " | LEVEl: ", acc_level)
    print("AccountID: ", acc_id)
    print("\nCURRENT RANKS: ")

    for rank in ranked_info:
        queue = ''
        if rank['queueType'].count('SOLO'):
            queue = "Solo Queue:\t"
        elif rank['queueType'].count('FLEX'):
            queue = "Flex Queue:\t"
        print(queue, rank["tier"], rank["rank"], rank['leaguePoints'], "lp |", "WINS: ", rank['wins'], "| LOSSES:", rank['losses'], " | Win Ratio: ", winLossRatio(rank['wins'], rank['losses']))

        

    print("\nMASTERY:")
    print("Total Champions: ", len(champ_list))
    #champAmount = int(input("\nHow many champions do you want to see?:"))
    print("RANK                NAME | MASTERY")
    print("----------------------------------")
    #for i in range(champAmount) :
    for i in range(0, 30) :
        champ_points = mastery_info[i]['championPoints']
        champ_id = mastery_info[i]['championId']
        champ_level = mastery_info[i]['championLevel']
        for Champion in champ_list :
            if champ_id == int(Champion.return_key()) :
                print('Rank {0:<3} {1:>15} | Level {2:<1} - {3:,}'.format(i+1, Champion.return_name(), champ_level, champ_points))
    
    print("\nMATCH HISTORY")
    print("Past 20 games:")
    GoThroughHistory(0, 20)
    print("\n21st - 40th")
    GoThroughHistory(21, 40)

else:
    print('[!] Request Failed')

print("\n")