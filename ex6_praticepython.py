#ex6 praticepython.org
wyraz=str(input("Prosze, podaj jeden wyraz: "))
zaryw=wyraz[::-1]
if wyraz==zaryw:
    print("to jest palindrom")
else:
    print("to nie jest palindrom")