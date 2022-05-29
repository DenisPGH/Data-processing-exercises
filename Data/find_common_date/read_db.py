from datetime import datetime

import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="TEST",
    user="denis_postgre",
    password="D_12-K9")



cur = con.cursor()





wished_date ='2000-03-02'
wished_date = datetime.strptime(f'{wished_date}', '%Y-%m-%d')
dict_query={'a':wished_date,}

#a=cur.execute('SELECT * FROM employees ORDER BY date(start_date) DESC Limit 1')
#a=cur.execute('SELECT * FROM  employees ORDER BY end_date DESC ')
a=cur.execute('SELECT * FROM  employees WHERE project=4 AND start_date > %(a)s ',dict_query)
a = cur.fetchall()
print(len(a))
print(a)
# for r in a:
#     print(r)


con.close()


