from datetime import datetime

import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="TEST",
    user="denis_postgre",
    password="D_12-K9")



cur = con.cursor()





wished_date ='2000-03-02'
wished_date_end ='2005-03-02'
wished_date = datetime.strptime(f'{wished_date}', '%Y-%m-%d')
wished_date_end = datetime.strptime(f'{wished_date_end}', '%Y-%m-%d')
dict_query={'a':wished_date,
            'b':wished_date_end}

#a=cur.execute('SELECT * FROM employees ORDER BY date(start_date) DESC Limit 1')
#a=cur.execute('SELECT * FROM  employees ORDER BY end_date DESC ')
#a=cur.execute('SELECT * FROM  employees WHERE project=4 AND start_date > %(a)s ',dict_query)
#a=cur.execute('SELECT * FROM  employees WHERE project=3 ORDER BY end_date-start_date DESC LIMIT 2',dict_query)
#a=cur.execute('SELECT f1.* FROM employees f1 WHERE exists (select 1 FROM employees f2 where tsrange(f2.start_date, f2.end_date ) AND tsrange(f1.start_date, f1.end_date) and f2.project = f1.project)')
#a=cur.execute('SELECT f1.* FROM employees f1 WHERE project=3 and exists (select 1 FROM employees f2 where f1.start_date in (f2.start_date, f2.end_date ) AND f2.start_date in (f1.start_date, f1.end_date) and f2.project = f1.project)')
bbbb=cur.execute('SELECT f1.* FROM employees f1 WHERE '
              'exists (select 1 '
              'FROM employees f2 '
              'WHERE f1.start_date=f2.start_date '
              'AND f2.project = f1.project AND f2.employee <> f1.employee)')

a=cur.execute('SELECT f1.* FROM employees f1 WHERE '
              'exists (select 1 '
              'FROM employees f2 '
              'WHERE tsrange(f2.start_date, f2.end_date)  && tsrange(f1.start_date, f1.end_date) '
              'AND f2.project = f1.project '
              'AND f2.employee <> f1.employee)')

a = cur.fetchall()
print(len(a))
print(a)
for r in a:
    print(f"{r[3]},{r[2]}")
    print(f"{r[2]-r[3]}")


con.close()


