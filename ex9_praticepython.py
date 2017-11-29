#ex9_praticepython

import random
pytanko=int(input("Wprowadz liczbe od 1 do 9: "))
losowanie=random.randint(1,9)
roznica=abs(losowanie-pytanko)
if roznica==0:
    print("Gorąco, wygrales!")
elif (roznica>0 and roznica<=2):
    print("Ciepło")
elif (roznica>2 and roznica<=4):
    print("Chłodno")
elif (roznica>4 and roznica<=6):
    print("Zimno")
else:
    print("Lodowiec, przegrales, sprobuj jeszcze raz")
    