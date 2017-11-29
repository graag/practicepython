#ex3 praticepython.org
#a=[1,1,2,3,5,8,13,21,34,55,89]
ciag=[1,2]
for i in range(8):
    ciag.append(ciag[i]+ciag[i+1])
nowa=[]    
for num in ciag:
    if num < 5:
        nowa.append(num)
print(nowa)

