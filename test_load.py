import pandas as pd
import sqlite3

conn = sqlite3.connect("churn.db")
query = "SELECT * FROM Customers"
df = pd.read_sql(query, conn)
conn.close()

print(f"Number of rows: {len(df)}")
print(df.info())
