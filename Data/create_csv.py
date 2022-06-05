import csv

range_a=100000
range_b=100001

with open('file_a.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    for a in range(range_a):
        employee_writer.writerow([f'John{a}'])

with open('file_b.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    for a in range(range_b):
        if a==9:
            continue
        employee_writer.writerow([f'John{a}'])

