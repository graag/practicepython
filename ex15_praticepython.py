#ex15
def powiedz(n):
    
    #dziele
    y=n.split()
    #odwracam
    y.reverse()
    # zwracam polaczone
    return " ".join(y)
zadanie=str(input("Napisz prosze dlugie zdanie: "))
     #wywoluje funkcje
m=powiedz(zadanie)    
