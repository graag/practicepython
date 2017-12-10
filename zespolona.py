# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:39:05 2017

@author: Anna
"""

class Complex:
    def __init__(self,real,imag):
        self.r=real
        self.i=imag
        print(self.r, ',', self.i,'i')
    def __add__(self,sample):
            return Complex(sample.r+self.r,sample.i+self.i)
    def modul(self):
        #print(self.r**2 + self.i**2)
        return self.r**2 + self.i**2

        

my_real=int(input("Put real part of complex number: "))
my_imag=int(input("Put imag part of complex number: "))

modul_complex=Complex(my_real,my_imag).modul()


add_complex=my_real.__add__(my_imag)


print("Modul of complex number is: ",modul_complex)
print("Addition of complex number is: ",add_complex)