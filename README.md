# commander-template
Adds all the boring cards to a .cod file

# prereq
`pip install pandas`

# install
open a command prompt

`git clone https://github.com/DrAtomic/commander-template.git`

then go into that directory 

`cd commander-template`

# usage
## tldr
`python commander.py <name_of_deck> <colors>`

so something like 

`python commander.py jund rbg`

easy

## in depth

The program looks at the cards.csv file. If you feel like something is missing just add the cards in there. use notepad or whatever you like. If you think a card needs to be added to every deck then under type put all

for example lets say you think [tibalt the fiend-blooded](https://scryfall.com/card/ddk/41/tibalt-the-fiend-blooded) should be in every deck. what you would need to do to add this card to every deck is simple add this line at the bottom of cards.csv
`Tibalt the Fiend-Blooded,r,all`
Notice that the capitalization on the card must be correct and that there are no spaces inbetween the commas 
