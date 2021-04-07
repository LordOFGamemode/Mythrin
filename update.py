import sqlite3
import time
import spe
count = 0
while True:
    text = spe.from_mic()
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE displaydata SET text=(?) WHERE 1",(text,))
    conn.commit()
    conn.close()
    count += 1
    time.sleep(0.1)