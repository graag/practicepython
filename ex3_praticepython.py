# changed ex3 praticepython.org
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--input","-i",help="file", required=True)
args=parser.parse_args()
with open(args.input) as f:
    data = json.load(f)
    for j in data:
        if j<5:
            print(j)