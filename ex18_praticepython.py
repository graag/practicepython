#ex18   #rules: https://en.wikipedia.org/wiki/Bulls_and_Cows
import random

def compare(lottery,guess):
    cowbull=[0,0]   #index zero = bull, index 1 = cow
    
    for i in range(len(lottery)):
      for j in range(len(lottery)):
        if int(guess[i]) == lottery[j]:
          if i == j:
              cowbull[0]+=1
              guess[i]=10
          if i != j:
              cowbull[1]+=1
    return cowbull       

if __name__=="__main__":
    playing = True #gotta play the game
    lottery=random.sample(range(0,9),4)  #random.sample gives me unique digits 
#    lottery=[1,2,3,4]
    score = 0

    while playing:
        lista=set()
        guess = list(input("Give me your best guess! The 4 digits must be all different. If the matching digits are in their right positions, they are bulls, if in different positions, they are cows.\n"))
        guess = [int(i) for i in guess]

        guess=list(guess)
        unique = [x for x in guess if x not in lista and (lista.add(x) or True)]
        
        guess=list(guess)
        for i in guess:
            if len(guess)!=4 or len(unique)!=4:
                guess = list(input("You didnt put unique values or you put less than 4 or more than 4 digits. Try one more time and remember the digits must be all different. If the matching digits are in their right positions, they are bulls, if in different positions, they are cows.\n"))
            else:
                continue
        
        if guess == "exit":
            break
        else:
            #guess=list(guess)
            cowbullcount = compare(lottery,guess)
            score+=1
                        
            print("You have "+ str(cowbullcount[0]) + " bulls, and " + str(cowbullcount[1]) + " cows.")
                
            if cowbullcount[0]==4:
                playing = False
                print("You win the game after " + str(score)+'. '+ 'The number was: '+ str(lottery))
                break #redundant exit
            else:
                print("Your guess isn't quite right, try again.")