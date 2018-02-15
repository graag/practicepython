#ex2 praticepython.org
#Excercice 2 - zadanie dodatkowe



notok=True
while notok:
    try:
        ask_number=int(input("Please,type number: "))
        notok=False
    except ValueError:
        print("I didn't type any number. Try again")
        

if ask_number%2==0:
    print("You typed even number")
    if ask_number%4==0:
        print("and number is divided by 4")
else:
        print("This number is odd")

#I used while loop and try and except command