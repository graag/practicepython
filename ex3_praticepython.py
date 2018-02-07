# changed ex3 praticepython.org

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()

array = [1,1,2,3,5,8,13,21,34,55,89]

with open("array.json","w") as f:
    json.dump(array,f)    

with open("array.json") as f:
    data=json.load(f)
    for i in data:
        if i<5:
            print(i)