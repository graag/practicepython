# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:08:47 2017

@author: Anna
"""

#ex18

import random

ra=[]
for i in range(4):
    i=random.randint(0,9)
    ra.append(i)

stra=''.join(str(e) for e in ra)
zgadnij=list(input("Podaj liczbe czterocyfrowa: "))
nowa=[]
for item in zgadnij:
    nowa.append(int(item))

def porownanie(ra,nowa):
    krowabyk=[0,0]
    for i,ra_val in enumerate(ra):
        #print (i,ra_val)
        for j,nowa_val in enumerate(nowa):
            if ra_val==nowa_val and i==j:
                krowabyk[0]+=1
            elif ra_val==nowa_val and i!=j:
                krowabyk[1]+=1
            
    return krowabyk            

wynik=porownanie(ra,nowa)