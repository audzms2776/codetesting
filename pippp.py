from tqdm import tqdm
import subprocess
import csv
import sys
import time

def process_func(file_name):
    f = open('notes/note.csv', 'r', encoding='utf-8')
    csv_reader = csv.reader(f)
    flag = True
    #pbar = tqdm(total=200)
    start_time = time.time()

    for line in csv_reader:
        result = str(subprocess.check_output(file_name, input=str.encode(line[0]), shell=True))
        result = result[2:-1]

        if result != line[1]:
            flag = False
            #pbar.close()
            break
    
        #pbar.update(1)
    
    return flag, time.time() - start_time

p1 = process_func(sys.argv[1])
p2 = process_func(sys.argv[2])

if p2[0]:
    print(
    '''
    Good
    {}: {}
    {}: {}
    '''.format(sys.argv[1], p1[1], sys.argv[2], p2[1])
    )
else:
    print('Fail')
