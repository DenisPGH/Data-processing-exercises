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
# bbbb=cur.execute('SELECT f1.* FROM employees f1 WHERE '
#               'exists (select 1 '
#               'FROM employees f2 '
#               'WHERE f1.start_date=f2.start_date '
#               'AND f2.project = f1.project AND f2.employee <> f1.employee)')

a=cur.execute('SELECT f1.* FROM employees f1 WHERE '
              'exists (select 1 '
              'FROM employees f2 '
              'WHERE tsrange(f2.start_date, f2.end_date)  && tsrange(f1.start_date, f1.end_date) '
              'AND f2.project = f1.project '
              'AND f2.employee <> f1.employee)')

a = cur.fetchall() # list of tuples
print(len(a))
#print(a)

# for r in a:
#     print(f"{r[2]},{r[3]}")
#     print(f"{r[2]-r[3]}")

latest_start = max(a[0][2], a[1][2])
earliest_end = min(a[0][3], a[1][3])
delta = (earliest_end - latest_start).days
overlap = max(0, delta)
#print(overlap)
#print("next")

all_pairs={}
longest_period_together=0

if a:
    for each in range(len(a)):
        for other in range(len(a)):
            if each==other:
                continue
            if a[each][1]==a[other][1]:
                latest_start = max(a[each][2], a[other][2])
                earliest_end = min(a[each][3], a[other][3])
                delta = (earliest_end - latest_start).days
                overlap = max(0, delta)
                if overlap>longest_period_together:
                    all_pairs[overlap]=[a[each][0],a[other][0],a[each][1]]
                    #print(all_pairs[overlap])

period,employees_=sorted(all_pairs.items(),key=lambda x:(-x[0]))[0]

print(f"The longest is {period} days, the emp are {', '.join([str(x) for x in employees_[:2]])},id={employees_[2]} ")


# prove the result

first_empl_name=employees_[0]
second_empl_name=employees_[1]
id=employees_[2]
dict_query={'first_':first_empl_name,
            "second_":second_empl_name,
            'id':id}
result_a=cur.execute('SELECT * FROM  employees WHERE  employee=%(first_)s AND project=%(id)s ',dict_query)

#result=cur.execute('SELECT * FROM employees WHERE project=1')
result_a=cur.fetchall()
result_b=cur.execute('SELECT * FROM  employees WHERE  employee=%(second_)s AND project=%(id)s ',dict_query)

#result=cur.execute('SELECT * FROM employees WHERE project=1')
result_b=cur.fetchall()

print(result_a[0][2],result_a[0][3],result_a[0][1])
print(result_b[0][2],result_b[0][3],result_a[0][1])



con.close()
cur.close()


# latest_start = max(a[0][2], a[1][2])
# earliest_end = min(a[0][3], a[1][3])
# delta = (earliest_end - latest_start).days
# overlap = max(0, delta)
# print(overlap)


