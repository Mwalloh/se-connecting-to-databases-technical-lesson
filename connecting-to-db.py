import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

cur = conn.cursor()

df = pd.DataFrame(
    cur.execute("""SELECT * FROM offices;""").fetchall(),

    columns=[x[0] for x in cur.description]
)

print(df)

conn.close()