# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:50:09 2017

@author: Anna
"""
import numpy as np
import matplotlib.pyplot as plt

lista=[1,2,3,4,5]
# tworzy wektory z list
arr1=np.array(lista)
arr2=np.array([
            [2,4,5,6,1],
            [3,2,5,6,1],
            [3,5,4,6,2]
            ])
print(arr1+arr2)
print(arr2.shape)
Narray=np.zeros(shape=(10,10,10))
#slice, okrajanie macierzy
print(Narray[0,5:8,1:3])
macierz=np.arange(25).reshape(5,5)


#wyciaganie elementow zz macierzy
print(macierz[macierz>10])
#wpisuje false w macierz
print(macierz>10)
print(macierz[macierz%2==0])
print(macierz*10)
print(np.diag(macierz))
#print(macierz.T)
# len -> zwraca pierwszy wymiar
#print(len(macierz))
# size-> zwraca wielkosc macierzy
#print(macierz.size)\
# w macierzach rowniez indexowanie od 0


print(np.where(macierz>10))
print(macierz[np.where(macierz>10)])


x=np.arange(-np.pi*2,np.pi*2,0.01)
s=np.sin(x)
c=np.cos(x)
plt.plot(x,s)
plt.show()