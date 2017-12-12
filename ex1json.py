#ex3 praticepython.org
#a=[1,1,2,3,5,8,13,21,34,55,89]

#JSON
"""Zapoznaj się z formatem json: https://www.w3schools.com/js/js_json_intro.asp
Zapoznaj się z biblioteką argparse
dopisz obsługę parametru lini komend -h / --help - wypisuje tekst pomocy
dopisz obsługę parametr -i / --input który pobiera nazwę pliku json
Dopisz wczytywanie tablicy z pliku json"""

#series=[1,2]
#for i in range(8):
#    series.append(series[i]+series[i+1])
#new=[]    
#for num in series:
#    if num < 5:
#        new.append(num)
#print(new)

#import json

import argparse
def Main():
    #I add -- to define optional arguments
    #calling by --number1 2 --number2 5 --operation add
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1",help="first number")
    parser.add_argument("--number2",help="second number")
    parser.add_argument("--operation",help="operation", choices=["add","subtract","multiply"])

    args = parser.parse_args()
    print(args)
    print(args.number1)
    print(args.number2)
    print(args.operation)
    
    n1=int(args.number1)
    n2=int(args.number2)
    result=None
    if args.operation=="add":
        result=n1+n2
    elif args.operation=="subtract":
        result=n1-n2
    elif args.operation=="multiply":
        result=n1*n2
    else:
        print("unsupported operation")
    print("Result is: ",result)
if __name__=='__main__':
    Main()
    


