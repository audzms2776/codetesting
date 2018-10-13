import subprocess
import csv
import sys
from tqdm import tqdm


f = open('csv_gen/false_note.csv', 'r', encoding='utf-8')
f2 = open('csv_gen/test_note.csv', 'w', encoding='utf-8')
csv_reader = csv.reader(f)
csv_writer = csv.writer(f2)

for line in tqdm(csv_reader):
    result = str(subprocess.check_output(sys.argv[1], input=str.encode(line[0]), shell=True))
    result = result[2:-1]
    csv_writer.writerow([line[0], result])

f.close()
f2.close()
