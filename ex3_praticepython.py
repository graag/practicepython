# changed ex3 praticepython.org
import argparse
import string as st

parser = argparse.ArgumentParser()
parser.add_argument("--input","-i",help="file", type=argparse.FileType('r'))
args=parser.parse_args()
sas=args.input.read()

sas.translate(st.punctuation)
print(sas)
sas=sas[1:(len(sas)-1)]
sas2 = sas.split(',')
str.maketrans
sas2 = [int(i) for i in sas2]
print(sas2)
print(type(sas2))
for j in sas2:
    if j<5:
        print(j)