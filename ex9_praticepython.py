#ex9_praticepython
#Excercise 9 - zadanie dodatkowe #4

import random
in_game=True
ask = None
score=0
while in_game:
    ask=input("Type number from 0 to 9. If you want exit type: exit  ")
    score+=1
    if ask != 'exit':
        ask = int(ask) 
    else:
        in_game = False
    if in_game:
        lottery=random.randint(1,9)
        difference=abs(lottery-ask)
        if difference==0:
            print("Hot, You won!")
        elif (difference>0 and difference<=2):
            print("Hotter")
        elif (difference>2 and difference<=4):
            print("Cool")
        elif (difference>4 and difference<=6):
            print("Cooler")
        else:
            print("Too cold, You failed. Try again")
print("Number of attempts: ",score)        