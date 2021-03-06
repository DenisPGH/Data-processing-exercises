from datetime import datetime

import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="TEST",
    user="denis_postgre",
    password="D_12-K9")



cur = con.cursor()
cur.execute('DROP TABLE employees')
cur.execute('''CREATE TABLE employees
               (employee integer unique , project integer , start_date DATE , end_date DATE )''')
counter=1
with open('test.csv','r') as file:
    for row in file.readlines():
        row=row.split(", ")
        end_strip=row[3].strip('\n')
        id_emp=int(row[0])
        id_project=int(row[1])
        start = datetime.strptime(f'{row[2]}', '%Y-%m-%d')
        end = datetime.strptime(f"{end_strip}", '%Y-%m-%d')
        dict_query={'a':counter,
                    'b':id_project,
                    'c':start,
                    'd':end}


        cur.execute('INSERT INTO employees(employee,project,start_date,end_date )'
                    ' VALUES(%(a)s, %(b)s, %(c)s, %(d)s)', dict_query)
        counter+=1
        # except:
        #
        #     # cur.execute('UPDATE employees SET start_date = %(c)s,end_date = %(d)s '
        #     #             'WHERE employee=%(a)s',dict_query)



con.commit()
con.close()
cur.close()