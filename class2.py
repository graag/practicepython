# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:00:36 2017

@author: Anna
"""
#self-> funkcja przyjmuje wartosci obiektu

#lub class Wektor()
class Wektor(object):
    "Dwuwymiarowy wektor"
    def __init__(self,x,y):
        self.a=x
        self.b=y
        print("wektor zostal stworzony")
    def dlugosc(self):
        "zwraca dlugosc wektora"
        return (self.a**2+self.b**2)**0.5
    #definiujemy jak ma wyprintowac
    def __str__(self):
        return "[{},{}]".format(self.a,self.b)
    #definiujemy operator dodawania
    def __add__(self,other):
        return Wektor(self.a+other.a,self.b+other.b)
w1=Wektor(3,2)    
w2=Wektor(5,7)
#print(w1.dlugosc())
print(w1)
print(w2)
print(w1.__add__(w2))
#lub
print(w1+w2)
class Prostokat:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def pole(self):
        "zwraca dlugosc wektora"
        return self.a * self.b

class Kwadrat(Prostokat):
    def __init__(self,x):
        self.a=x
        self.b=x

pole1=Prostokat(3,3).pole()
pole2=Kwadrat(3).pole()
print(pole1,pole2)


class Prostokat2(Prostokat):
    def obwod(self):
        return 2*self.a+2*self.b
obwod_prostokata=Prostokat2(3,4).obwod()
print(obwod_prostokata)