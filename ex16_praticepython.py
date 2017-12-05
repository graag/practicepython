# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:51:28 2017

@author: Anna
"""

#ex16
import string
import random

def password(dlugosc,chars=string.ascii_letters+string.ascii_lowercase+string.punctuation+string.digits):
    return "".join(random.choice(chars) for _ in range(dlugosc))


dlugosc=int(input("Jak dlugie ma byc twoje haslo? 8 znaków? 9? 10?: "))

print(password(dlugosc))