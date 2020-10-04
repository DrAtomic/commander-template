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
    tesat = ["".join(map(str,comb)) for comb in permutations(color,2)]
    for c in tesat:
        for i in dictionary:
            if c in i.get('Colors'):
                temp.append(i)
    result = [x for x in temp if x is not None]
    return(result)



if __name__ == "__main__":
    
    df = pd.read_csv('cards.csv')
    test = df.to_dict(orient='records')
    name = str(sys.argv[1])
    colors = list(sys.argv[2])
    temp =[]
    x = color_or(test, colors)
    fetchlands=[]
    for i in x:
        fetchlands.append(fetch(i))
    fetchlands = [t for t in fetchlands if t is not None]
    fetchlands = [dict(t) for t in {tuple(d.items()) for d in fetchlands}]

    basics = []
    for i in x:
        if any(t == "basic" for t in i.values()):
            basics.append(i)
    
    y = color_and(test,colors)

    auto_include = []
    for i in x:
        if any(t == "all" for t in i.values()):
            auto_include.append(i)
            
    listoflands = []
    for i in fetchlands:
        listoflands.append(i.get('Title'))

    for i in y:
        listoflands.append(i.get('Title'))

    for i in auto_include:
        listoflands.append(i.get('Title'))

    for i in basics:
        listoflands.append(i.get('Title'))

    mylist = list(dict.fromkeys(listoflands))
    f = open(str(name)+".cod",'w')
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<cockatrice_deck version=\"1\">\n\t<deckname></deckname>\n\t<comments></comments>\n\t<zone name=\"main\">\n")
    for name in mylist:
        f.write("\t\t<card number=\"1\" name=\""+str(name)+"\"/>\n")
    f.write("\t</zone>\n</cockatrice_deck>")
    f.close()

