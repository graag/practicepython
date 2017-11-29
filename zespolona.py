# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:39:05 2017

@author: Anna
"""

class Zespolona:
    def __init__(self,rz,ur):
        self.r=rz
        self.i=ur
        print(self.r, ',', self.i,'i')
    def __add__(self,cos):
            return Zespolona(cos.r+self.r,cos.i+self.i)
    def modul(self):
        print(self.r**2 + self.i**2)
