#zamiast 13 zadania z practicepython.org
#Ciag fibonacciego
import pylab as py

def fibo(n,l):
    suma=0
    ciag_f=[1,2]
    for i in range(n):
        nowy_element=ciag_f[-1]+ciag_f[-2]
        ciag_f.append(nowy_element)
        suma=suma+nowy_element
    return suma, ciag_f[l]
qwert=fibo(10,3)



py.figure()
py.plot(fibo)


