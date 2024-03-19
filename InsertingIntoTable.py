import sqlite3
conn=sqlite3.connect("SecondDataBase.db")
try:
    
    conn.execute("Drop table ManuCard")
    conn.commit()
except Exception as e:
    print(e)
print('data inserted successfully!')
conn.close()