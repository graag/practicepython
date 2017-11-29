#ex2 praticepython.org

ask_liczba=int(input("Proszę, podaj liczbę: "))
if ask_liczba%2==0:
    print("Podales liczbe parzysta")
    if ask_liczba%4==0:
        print("oraz liczbe podzielna przez 4")
else:
    print("Podales liczbe nieparzysta")
