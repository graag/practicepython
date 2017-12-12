#ex18
#import random

def compare(lottery,guess):
    #first cow (guess in the correct place ) bull (in wrong place)
    cowbull=[0,0]
    
    for i in range(4):
      for j in range(4):
        if guess[i] == lottery[j]:
          if i == j:
              cowbull[0]+=1
          elif guess[j] == lottery[j]:
              cowbull[1]=cowbull[1]      
          else:
              cowbull[1]+=1
#    for i,lottery_val in enumerate(lottery):
#        #print (i,lottery_val)
#        for j,guess_val in enumerate(guess):
#            
#            if lottery_val==guess_val:
#                if i==j:
#                    cowbull[0]+=1
#                else:
#                    cowbull[1]+=1
            
    return cowbull       

if __name__=="__main__":
    playing = True #gotta play the game
    #lottery=[]
    #for i in range(4):
    #    i=random.randint(0,9)
    #    lottery.append(i)    
    score = 0
    lottery2=[6, 1, 6, 8]

    while playing:
        guess2 = input("Give me your best guess!")
        if guess2 == "exit":
            break
        else:
            guess2=list(guess2)
            cowbullcount = compare(lottery2,guess2)
            score+=1
                        
            print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
                
            if cowbullcount[1]==4:
                playing = False
                print("You win the game after " + str(score) + "! The number was "+str(lottery2))
                break #redundant exit
            else:
                print("Your guess isn't quite right, try again.")
