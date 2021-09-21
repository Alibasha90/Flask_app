import sqlite3

conn = sqlite3.connect('sensor.db')
print("Opened database successfully")
cur =conn.cursor()

cur.execute('CREATE TABLE sensor(SENSOR_ID TEXT, LOCATION TEXT, INSTALLATION_DATE TEXT, OIL_COLOR TEXT,TRANSFORMER_OIL_COLOR TEXT)')
#print("Table created successfully")

#cur.execute("INSERT INTO students (name,addr,city,pin)
#VALUES(?, ?, ?, ?)",(nm,addr,city,pin) )

conn.commit()



conn.close()