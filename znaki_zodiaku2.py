#changed excercise znaki_zodiaku
import datetime
day_urodzenia=input("W jakim dniu się urodziłes?:  ")
day_urodzenia=int(day_urodzenia)
mc_urodzenia=input("W jakim miesiacu się urodziłes? podaj liczbę:  ")
mc_urodzenia=int(mc_urodzenia)
rok_urodzenia=input("W którym roku się urodziłes? podaj liczbę:  ")
rok_urodzenia=int(rok_urodzenia)
rezultat=datetime.date(rok_urodzenia, mc_urodzenia, day_urodzenia).strftime("%j")
rezultat=int(rezultat)

koziorozec2=list(range(1,20,1))  
wodnik=list(range(20,50,1))
ryby=list(range(50,80,1))
baran=list(range(80,110,1))
byk=list(range(110,141,1))
bliznieta=list(range(141,172,1))
rak=list(range(172,204,1))
lew =list(range(204,235,1))
panna=list(range(235,266,1))
waga=list(range(266,296,1))
skorpion=list(range(296,326,1))
strzelec=list(range(326,356,1))
koziorozec1=list(range(356,366,1))

znaki=[koziorozec2,wodnik, ryby, baran, byk, bliznieta, rak, lew, panna, waga, skorpion,strzelec,koziorozec1]
slownik={'koziorozec2':znaki[0],'wodnik':znaki[1],'ryby':znaki[2],'baran':znaki[3], 'byk':znaki[4], 'bliznieta':znaki[5], 'rak':znaki[6], 'lew':znaki[7], 'panna':znaki[8], 'waga':znaki[9], 'skorpion':znaki[10],'strzelec':znaki[11],'koziorozec1':znaki[12]}
for i in slownik:
    if rezultat in slownik[i]:
        print('Twoj znak zodiaku to: ',i)