import json
new=[]
array = '1,1,2,3,5,8,13,21,34,55,89'

with open("array5.json","w") as f:
    json.dump(array,f)    
