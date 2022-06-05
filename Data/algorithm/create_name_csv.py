import csv
import random
import string

with open('names.csv', mode='w',newline='') as file:
    #name_writer = csv.writer(employee_file, delimiter='.')
    for a in range(1000000):
        new_name=''.join([random.choice(string.ascii_letters),
                          random.choice(string.ascii_letters),random.choice(string.ascii_letters),
                          random.choice(string.ascii_letters),random.choice(string.ascii_letters)])
        file.write(new_name)
        file.write('\n')