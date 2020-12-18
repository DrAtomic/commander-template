import pandas as pd
from itertools import permutations
import sys

def search(values,searchFor):
    for k in values.get('Colors'):
        if searchFor in k:
            return values


def color_or(dictionary,color):
    temp =[]
    for color in colors:
        for i in dictionary:
            temp.append(search(i,color))
    result = [x for x in temp if x is not None]
    return result


def fetch(list_dictionaries):
    if any(t == "fetch" for t in list_dictionaries.values()):
        return list_dictionaries


def color_and(dictionary, color):
    temp = []
    perm = []
    for i in range(len(color)+1):
        perm.append(["".join(map(str,comb)) for comb in permutations(color,i)])
    flatten = lambda t: [item for sublist in t for item in sublist]
    perm = flatten(perm)
    for c in perm:
        for i in dictionary:
            if c == i.get('Colors'):
                temp.append(i)
    result = [x for x in temp if x is not None]
    return(result)



if __name__ == "__main__":
    
    df = pd.read_csv('cards.csv')
    cards_dict = df.to_dict(orient='records')        
    name = str(sys.argv[1])
    colors = list(sys.argv[2])

    full_dict = []
    for i in cards_dict:
        if any(t == "all" for t in i.values()):
            full_dict.append(i)
            
    x = color_or(cards_dict, colors)
    for i in x:
        full_dict.append(fetch(i))
        if any(t == "basic" for t in i.values()):
            full_dict.append(i)
        
    full_dict = [t for t in full_dict if t is not None]
    full_dict = [dict(t) for t in {tuple(d.items()) for d in full_dict}]

    y = color_and(cards_dict,colors)
    dict_of_cards = []
    for i in y:
       dict_of_cards.append(i.get('Title'))
    for i in full_dict:
       dict_of_cards.append(i.get('Title'))

    list_of_cards = list(dict.fromkeys(dict_of_cards))
    
    f = open(str(name)+".txt",'w')
    for name in list_of_cards:
        f.write(str(name)+"\n")
    f.close()
