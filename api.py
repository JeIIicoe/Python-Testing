import requests
import json
import urllib
from Champion import *

api_token = 'xxxxx'
api_url_base = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
api_mastery_url_base = 'https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'
api_ranked_url_base = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
api_match_history_url_base = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
api_game_url_base = 'https://euw1.api.riotgames.com/lol/match/v4/matches/'

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



def get_account_mastery(acc_id): #Gets an account's chamption mastery json list from an AccountID
    response_string = api_mastery_url_base + acc_id + '?api_key=' + api_token
    response = requests.get(response_string)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None



def get_account_rank(acc_id): #Gets an account's ranked stats from an AccountID
    response_string = api_ranked_url_base + acc_id + '?api_key=' + api_token
    response = requests.get(response_string)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8')) 
    else: 
        return None 
 
 
 
 
def get_match_history(acc_id): #Gets an account's match history json list from an AccountID
    response_string = api_match_history_url_base + acc_id + '?api_key=' + api_token # + ?champion= + {champId} /// + ?champion= + {champId} + &endIndex= + {int} /// + ?endIndex= + {int}
    response = requests.get(response_string)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

        

def get_match(match_id): #Gets a match from a match's id
    response_string = api_game_url_base + match_id
    response = requests.get(response_string)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None



def winLossRatio(wins, losses): #Calculates win/loss % ratio
    ratio = (wins / (wins + losses)) * 100 #wrong
    return round(ratio, 2)


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

    acc_id = account_info['id']
    acc_level = account_info['summonerLevel']
    acc_icon = account_info['profileIconId']
    acc_name = account_info['name']

    ranked_info = get_account_rank(acc_id)
    mastery_info = get_account_mastery(acc_id)

    print("-------------------------------------------")
    print("\nSUMMONER: ", acc_name, " | LEVEl: ", acc_level)
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
            #print("Champ ID: ", champ_id, "/", type(champ_id), " | ID of list champ: ", Champion.return_key(), "/", type(Champion.return_key()))
            if champ_id == int(Champion.return_key()) :
                #print('Rank: ', i+1, ': ', Champion.return_name(), 'Level:\t', champ_level, ': ', "{:,}".format(champ_points))
                print('Rank {0:<3} {1:>15} | Level {2:<1} - {3:,}'.format(i+1, Champion.return_name(), champ_level, champ_points))

else:
    print('[!] Request Failed')

print("\n")