# changed ex3 praticepython.org

import json
array={}
array = '{"numbers": [1,1,2,3,5,8,13,21,34,55,89]}'
data  = json.loads(array)
array2 = data['numbers']
print(array2)
s=json.dumps(array2)
with open("array.txt","w") as f:
    f.write(s)
with open("array.txt","r") as f:
    array3=json.load(f)
typ=type(array3)   
print(typ)