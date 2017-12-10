# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:04:14 2017

@author: Anna
"""

with open("prosty.txt",'r') as file:
    #print(file.read())
    for nr,line in enumerate(file):
        print(nr,line)
        #print(line.split(' '))
        slowa=line.split(' ')
        for i, slowo in enumerate(slowa):
            if slowo =="zł":
                budzet=slowa[i-1]
                print(budzet)
                
#nadpisanie pliku
#with open("prosty.txt",'w') as file:
                
