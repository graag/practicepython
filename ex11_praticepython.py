# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
#ex11
import sys
def prime():
    return int(input("Type number: "))

number = prime()
if number>1:    
    for i in range(2,number):
        if number%i!=0:
            continue
        elif number%i==0:
            sys.exit("This number isn't prime.")
            
    sys.exit("This number is prime")

elif number==0:
    sys.exit("You typed zero, could you type other number?")

""" When I changed this exercise I learnt a new library sys and command sys.exit.
 I think that in this exercise this command has the same function as print and break.
 Is it ok for you?"""         
        
#I changed variables from Polish to English