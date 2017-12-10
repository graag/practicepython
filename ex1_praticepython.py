#ex1 practicepython.org
import datetime

today=datetime.date.today().year
ask_name=input("What is your name?: ")
ask_age=int(input("How old are you?: "))
future=str(today+(100-ask_age))
print(ask_name+ ",in " +future +" you will celebrate your 100th birthday")
