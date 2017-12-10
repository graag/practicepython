# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:51:28 2017

@author: Anna
"""

#ex16
import string
import random

def password(length,chars=string.ascii_letters+string.ascii_lowercase+string.punctuation+string.digits):
#By command join we can join each string chars. 
#In this situation we join without any letter or space, if we change to "*", we receive string1*string2*string3 
#We can use "_" just as any other sign 
    return "".join(random.choice(chars) for _ in range(length))


length=int(input("How many sign should your password have? 8 signs? 9? 10?: "))

print(password(length))

    