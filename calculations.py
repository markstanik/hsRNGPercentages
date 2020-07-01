import pandas as pd
from probability import prob


# num_minions: number of minions you are summoning
# cost: cost of minion you are summoning (-1 if no cost)
# tag: the race of the minion you are summoning (ANY if no race)
# target_class: if discovering a minion the name of the class, otherwise ANY
# keyword: the keyword you are looking for
def summon(cards, num_minions, cost, race, target_class, keyword, rarity, discover):
    # summoning/mutating any minion, not discover
    minions_df = cards.loc[cards['type'] == 'MINION']
    parameters = [cost, race, target_class, rarity]
    json_names = ['cost', 'race', 'cardClass', 'rarity']
    for i in reversed(range(len(parameters))):
        if parameters[i] is None:
            del parameters[i]
            del json_names[i]
        else:
            minions_df = minions_df.loc[minions_df[json_names[i]] == parameters[i]]

    m_count = minions_df.shape[0]
    keyword_df = minions_df.loc[minions_df[keyword] == True]
    k_count = keyword_df.shape[0]
    output = prob(m_count, k_count, num_minions)
    return output

# card_type: if it is minion, spell, or weapon, or ALL
# mana: amount of mana you have to cast ideal card
# target class: class you are finding for, ALL_BUT for "from another class" effects
# tag: tag of minion you are adding, note: LEGENDARY is for dragons hoard
# def add_to_hand(cards, card_type, mana, target_class)

# --------------------------------------------------------------------------------------------------------------------------
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
