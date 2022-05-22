import csv

with open('file_a.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    for a in range(10):
        employee_writer.writerow([f'John{a}'])

with open('file_b.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    for a in range(11):
        if a==9:
            continue
        employee_writer.writerow([f'John{a}'])

