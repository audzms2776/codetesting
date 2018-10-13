import csv
import random
from tqdm import tqdm


f1 = open('str_note.csv', 'r', encoding='utf-8')
f2 = open('note.csv', 'w', encoding='utf-8')

wr = csv.writer(f2)
rd = csv.reader(f1)

data_arr = []

for ll in tqdm(rd):
    data_arr.append(ll)

random.shuffle(data_arr)

for data in tqdm(data_arr):
    wr.writerow(data)

f1.close()
f2.close()
