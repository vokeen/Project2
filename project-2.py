import os
from os import system
system("clear")

import random

wordbank = ['grumpish', 'groak', 'pismire' , 'crapulous' , 'snowbrowth' , 'excogigate' , 'apricity' , 'twattle' , 'elflock' , 'gorgonize' , 'cockalorum' , 'snoutfair' ,'jollux' , 'curglaff' , 'brabble' , 'twitterlight' ,'lunting' ,'beefwitted' ,'monsterful' ,'callipygian' , 'fuzzle' ,'quockerwodger' , 'resistentialism' , 'ethophobia' , 'sluberdegullion' , 'curmuring' , 'lumming' ,'californiawidow' ,'zenzizenzizenzic' ,'houppelande']

hints = ['an emotion ' , 'similar to croak' , 'close to a gem' , 'has the word crap in it' , 'season soup' , 'ex something' , 'close to electricity' , 'close to tattle' , 'el flock' ,'gor gon' , ' bird room' , 'dog nose' , 'jollux' , 'sounds like armor' , 'babble' , 'app light' , 'close to hunting' , 'meat smart' , 'monster' , 'calli' , 'close to fuzzy' , 'rodger' , 'resident' , 'scared of ethos' , 'sluber' , 'cur muring' , 'lumming' , 'cali single' , 'call of duty map' , 'hopping']

win =['Congrats You Won ' , 'Congradulations!!' , 'Winner!!' , 'Winner Winner Chicken Dinner' , 'You Won!!']
winner = random.choice(win)
lose =['You Lost :(','Im Dissapointed','TRY AGAIN','Run It Back...','Take Another Shot At It']
loser = random.choice(lose)
random = random.choice(wordbank)
index=wordbank.index(random)
item=int(index)
chances = len(random) + 2
c = str(chances)
word = [*random]
dash = []
for num in random:
    dash.append('-')
print(' '.join(dash))

i=1
while i < chances:
    i=i+1
    if '-' in dash:
        hint=print(hints[index])
        guess = input('Please type a letter: ')
        if guess in word:
            for num in range(len(word)):
                system('clear')
       
                if word[num] == guess:
                    dash[num] = guess
            print(' '.join(dash))
            print('Good Job , Keep Going')
        else:
            system('clear')
            print('That letter is not in the word , please keep trying')
            print(' '.join(dash))
if i == chances and '-' in dash:
    print(loser)
else:
    print(winner)

    


