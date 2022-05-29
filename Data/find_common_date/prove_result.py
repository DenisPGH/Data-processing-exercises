
import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="TEST",
    user="denis_postgre",
    password="D_12-K9")



curs = con.cursor()





result=curs.execute("SELECT * FROM employees where project=1")
result=curs.fetchall()


print(result)


con.close()
curs.close()
