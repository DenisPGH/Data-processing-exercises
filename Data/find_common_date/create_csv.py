import csv
import random

with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for a in range(300):
        spamwriter.writerow(
            [f'{random.randint(1,300)}',
             f' {random.randint(1,5)}',
             f' 200{random.randint(0,9)}-0{random.randint(1,9)}-{random.randint(0,2)}{random.randint(1,8)}',
             f" 201{random.randint(0,9)}"
             f"-0{random.randint(1,9)}-"
             f"{random.randint(0,2)}{random.randint(1,8)}"])


with open('test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

