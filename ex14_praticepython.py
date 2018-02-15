# ex14
# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

def funkcja(c):
    lista=[]
    for i in c:
        if i not in lista:
            lista.append(i)
        return lista
    
    
def funkcja2(c):
    return list(set(c))
a=[1,2,3,4,1,2,3,4,5,6,7,8,9]    
print(funkcja(a))    
print(funkcja2(a))    