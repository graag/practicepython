# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
#ex11
def prime():
    return int(input("Wybierz liczbe: "))

liczba = prime()
if liczba>1:    
    for i in range(2,liczba):
        if liczba%i==0:
            print("to nie jest liczba pierwsza")
            break
        else:
            print("to jest liczba pierwsza")
            break
        
