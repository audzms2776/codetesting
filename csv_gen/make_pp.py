import random
import string
import csv
from tqdm import tqdm


f = open('str_note.csv', 'w', encoding='utf-8')
wr = csv.writer(f)

base_arr = list(string.ascii_lowercase)

# True str
for i in tqdm(range(100)):
    random.shuffle(base_arr)
    str1 = ''.join(base_arr)
    wr.writerow([str1, "TRUE"])

f.close()
