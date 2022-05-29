import sqlite3
from datetime import datetime
import  pandas as pd






con = sqlite3.connect('employees.db')
cur = con.cursor()
a=cur.execute('SELECT * FROM employees ORDER BY date(start) DESC Limit 1')

for r in a:
    print(r)


con.close()


