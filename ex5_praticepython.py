#ex5 praticepython.org
a=[1,2]
for i in range(8):
    a.append(a[i]+a[i+1])

ab=list(range(1,14))
common=[]
for j in a:
    if j in ab:
        common.append(j)
print(a)
print(ab)
print(common)