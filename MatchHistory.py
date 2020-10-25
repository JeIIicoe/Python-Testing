import requests
import json
import urllib

api_match_history_url_base = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
api_game_url_base = 'https://euw1.api.riotgames.com/lol/match/v4/matches/'

def get_match_list(acc_id, api_token): #Gets an account's match history json list from an AccountID
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