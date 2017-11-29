#ex1 practicepython.org
import datetime

dzisiaj=datetime.date.today().year
ask_name=input("What is your name?: ")
ask_age=int(input("How old are you?: "))

year=str((dzisiaj-ask_age)+100)
print("Za sto lat "+ask_name +" bedzie miala "+ year+" lat")
