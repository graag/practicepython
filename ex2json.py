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

import json
book={}
book['tom']={
        'name':'tom',
        'address':'marszalkowska 1, Warsaw',
        'phone':'123456789'
}

book['bob']={
        'name':'bob',
        'address':'nowy swiat 21, Warsaw',
        'phone':'19283465'
}
s=json.dumps(book)
with open("C:/Users/Anna/Desktop/book.txt","w") as f:
    f.write(s)

#print(s)
    #mamy string
f=open("C:/Users/Anna/Desktop/book.txt","r")
ss=f.read()
print(ss)
 
#dostajemy dictionary
book2=json.loads(ss)
typ=type(book2)   
print(typ)
print(book['bob'])
print(book['bob']['phone'])

for i in book:
    print(book[i])