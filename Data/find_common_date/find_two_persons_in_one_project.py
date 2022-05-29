from datetime import datetime

import  pandas as pd

file=pd.read_csv('test.csv')
#print(file.head())


datetime_object = datetime.strptime('2005-01-01', '%Y-%m-%d')
print(datetime_object)


