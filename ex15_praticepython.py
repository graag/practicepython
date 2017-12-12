#ex15
def word(n):
    
    y=n.split()
    y.reverse()
    return " ".join(y)
sentence=str(input("Please, put long sentence: "))
     #call the function
result=word(sentence)    
print(result)