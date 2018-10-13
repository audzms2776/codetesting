from tqdm import tqdm
import random
import string
import csv


f = open('false_note.csv', 'w', encoding='utf-8')
wr = csv.writer(f)

base_arr = list(string.ascii_lowercase)

for i in tqdm(range(100)):
    my_str = ''

    for j in range(26):
        c = random.choice(base_arr)
        my_str += c
        
    wr.writerow([my_str])

f.close()
