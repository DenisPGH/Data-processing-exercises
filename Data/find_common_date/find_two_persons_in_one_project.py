from datetime import datetime

import  pandas as pd
import sqlite3

file=pd.read_csv('test.csv')
#print(file.head())
datetime_object = datetime.strptime('2005-01-01', '%Y-%m-%d')
con = sqlite3.connect('employees.db')
cur = con.cursor()
cur.execute('DROP TABLE employees')
cur.execute('''CREATE TABLE employees
               (employee integer , project integer , start TEXT ,end text )''')

cur.execute("INSERT INTO employees VALUES (1,1,'2000-09-01','2000-01-01')")
con.commit()
con.close()



#print(datetime_object)

con = sqlite3.connect('employees.db')
cur = con.cursor()
a=cur.execute('SELECT * FROM employees ORDER BY date(start) DESC Limit 1')

for r in a:
    print(r)
# print(a.)

con.close()


