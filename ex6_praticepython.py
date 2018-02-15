#ex6 praticepython.org
word=str(input("Please, put one word: "))
drow=word[::-1]
#drow=word[::-1]

#if I changed drow=word[::-2], we received reversed word with every second element,
#e.g. We typed word: warsaw , We received: wsa
print(drow)


if word==drow:
    print("This is Palindrom")
else:
    print("This isn't Palindrom")