import requests
import pandas as pd
from flask import Flask, render_template
def create_list():
    response = requests.get('https://api.hearthstonejson.com/v1/51510/enUS/cards.collectible.json')
    #get all standard cards into a list
    cards = response.json()
    std_sets = ['CORE', 'EXPERT1', 'DALARAN', 'DEMON_HUNTER_INITIATE', 'ULDUM', 'DRAGONS', 'YEAR_OF_THE_DRAGON', "BLACK_TEMPLE"]
    std_cards= [i for i in cards if i['set'] in std_sets]
    mech_list = ['BATTLECRY', 'TAUNT', 'DIVINE_SHIELD', 'COMBO', 'DEATHRATTLE', 'DISCOVER', 'ADJACENT_BUFF', 'AURA', 'CANT_BE_TARGETED_BY_HERO_POWERS', \
                'CHARGE', 'CHOOSE_ONE', 'COUNTER', 'ENRAGED', 'FREEZE', 'IMMUNE','POISONOUS','RUSH', 'SECRET', 'SILENCE', 'STEALTH', 'WINDFURY']
    for j in std_cards:
        for mech in mech_list:
            j[mech] = 'mechanics' in j and mech in j['mechanics']
    df = pd.DataFrame(std_cards)
    return df