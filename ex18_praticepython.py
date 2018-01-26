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
    score = 0

    while playing:
        guess = list(input("Give me your best guess! The digits must be all different. If the matching digits are in their right positions, they are bulls, if in different positions, they are cows."))
        guess = [int(i) for i in guess]
        if guess == "exit":
            break
        else:
            guess=list(guess)
            cowbullcount = compare(lottery,guess)
            score+=1
                        
            print("You have "+ str(cowbullcount[0]) + " bulls, and " + str(cowbullcount[1]) + " cows.")
                
            if cowbullcount[0]==4:
                playing = False
                print("You win the game after " + str(score)+'. '+ 'The number was: '+ str(lottery))
                break #redundant exit
            else:
                print("Your guess isn't quite right, try again.")