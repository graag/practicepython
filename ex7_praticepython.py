#ex7 praticepython.org

list1=list(range(1,11))
list2=[]
list3=[]
for i in list1:
    list2.append(i**2)
#long version  
for i in list2:    
    if i%2==0:
        list3.append(i) 
#short version: create list comprehension
list4=[item for item in list2 if item%2==0]        
        
print(list2)
print(list3)
print(list4)
    
    