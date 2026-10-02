import pandas as pd
import numpy as np
import sqlite3 as sql

file = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'

db = pd.read_csv(file)

connection = sql.connect('churn.db') #creates churn.db when ran
db.to_sql("Customers", connection, if_exists='replace', index=False)
cur = connection.cursor()
connection.close
