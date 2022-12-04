import sqlite3
import pandas as pd

DATABASE_PATH="../shipsdata.db"
# DATABASE_PATH="tempdb.db"
conn = sqlite3.connect(DATABASE_PATH)


ship_data = pd.read_csv(".\ships.csv")
ship_data.to_sql("ships", conn, if_exists='replace')


shipsposition_data = pd.read_csv(".\shipsposition.csv")
shipsposition_data.to_sql("shipsposition", conn, if_exists='replace')

cur = conn.cursor()

for row in cur.execute("SELECT * FROM ships"):
    print(row)

for row in cur.execute("SELECT * FROM shipsposition"):
    print(row)