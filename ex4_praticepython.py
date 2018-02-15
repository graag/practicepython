#ex4 praticepython.org
liczba=int(input("Prosze, podaj liczbe: "))
lista=[]
#od 1 bo uwazam na zero!
for i in range(1,liczba+1):
    if liczba%i ==0:
        lista.append(i)
print(lista)    