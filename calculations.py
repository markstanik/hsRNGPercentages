import pandas as pd
from probability import prob

#num_minions: number of minions you are summoning
#cost: cost of minion you are summoning (-1 if no cost)
#tag: the race of the minion you are summoning (ANY if no race)
#target_class: if discovering a minion the name of the class, otherwise ANY
#keyword: the keyword you are looking for
def summon(cards, num_minions, cost, race, target_class, keyword):
    #summoning/mutating any minion, not discover
    if cost != -1 and race == 'ANY' and target_class == 'ANY':
        total_df = cards.loc[(cards['cost'] == cost) & (cards['type'] == 'MINION')]
        t_count = total_df.shape[0]
        print(t_count)
        keyword_df = total_df.loc[total_df[keyword] == True]
        k_count= keyword_df.shape[0]
        print(k_count)
        output = prob(t_count, k_count, num_minions)
        print(output)
        return output
    #summoning where cost does not matter, not including Crown
    if race != 'LEGENDARY' and target_class == 'ANY':
        if cost == -1:
            total_df = cards.loc[cards['race'] == race]
        else:
            total_df = cards.loc[(cards['race'] == race) & (cards['cost'] == cost)]
        t_count = total_df.shape[0]
        keyword_df = total_df[total_df[keyword] == True]
        k_count = keyword_df.shape[0]
        output = prob(t_count, k_count, num_minions)
        print(output)
        return output
    #discovering and then summoning, currently only PoC and Crown
    if race == 'LEGENDARY':
        if target_class != 'ANY':
            total_df = cards.loc[(cards['rarity'] == race) & (cards['type'] == 'MINION') & ((cards['cardClass'] == target_class) | (cards['cardClass'] == 'NEUTRAL'))]
        else:
            total_df = cards.loc[(cards['rarity'] == race) & (cards['type'] == 'MINION')]
    else:
        total_df = cards.loc[(cards['cost'] == cost) & (cards['type'] == 'MINION') & ((cards['cardClass'] == target_class) | (cards['cardClass'] == 'NEUTRAL'))]
    t_count = total_df.shape[0]
    keyword_df = total_df[total_df[keyword] == True]
    k_count = keyword_df.shape[0] + 1
    output = prob(t_count, k_count, num_minions)
    return output
#card_type: if it is minion, spell, or weapon, or ALL
#mana: amount of mana you have to cast ideal card
#target class: class you are finding for, ALL_BUT for "from another class" effects
#tag: tag of minion you are adding, note: LEGENDARY is for dragons hoard
#def add_to_hand(cards, card_type, mana, target_class)

#--------------------------------------------------------------------------------------------------------------------------
# def power_of_creation(cards):
#     #only need 6 cost minions
#     total_df = cards.loc[(cards['cost'] == 6) & (cards['type'] == 'MINION') & ((cards['cardClass'] == 'MAGE') | (cards['cardClass'] == 'NEUTRAL'))]
#     print("Choose what type of minion you want")
#     keyword = input()
#     if keyword == 't':
#         success = total_df.loc[total_df['TAUNT'] == True].shape[0]
#     elif keyword == 'r':
#         success = total_df.loc[total_df['RUSH'] == True].shape[0]
#     elif keyword == 'c':
#         success = total_df.loc[total_df['CHARGE'] == True].shape[0]
#     elif keyword == 'u':
#         success = total_df.loc[total_df['CANT_BE_TARGETED_BY_HERO_POWERS'] == True].shape[0]
#     elif keyword == 'd':
#         success = total_df.loc[total_df['DEATHRATTLE'] == True].shape[0]
#     total = total_df.shape[0]
#     print(total)
#     print(success)
#     output = prob(total, success+1, 3)
#     print(output)
#     return output


