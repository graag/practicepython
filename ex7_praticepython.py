#ex7 praticepython.org
ta=list(range(1,11))
ta2=[]
ta3=[]
for i in ta:
    ta2.append(i**2)
    
for i in ta2:    
    if i%2==0:
        ta3.append(i) 
print(ta2)
print(ta3)
    
    