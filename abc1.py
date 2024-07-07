import sqlite3

conn = sqlite3.connect('database.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE criminaldata (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(20) NOT NULL,
                    father_name VARCHAR(25),
                    mother_name VARCHAR(25),
                    gender VARCHAR(6) NOT NULL,
                    dob VARCHAR(10),
                    blood_group VARCHAR(5),
                    identity_mark VARCHAR(30) NOT NULL,
                    nationality VARCHAR(15) NOT NULL,
                    religion VARCHAR(15) NOT NULL,
                    crimes VARCHAR(100) NOT NULL
                )''')

print("Table created successfully")

conn.execute("INSERT INTO criminaldata (id, name, father_name, mother_name, gender, dob, blood_group, identity_mark, nationality, religion, crimes) \
      VALUES (1, 'Paul', 'California', 'California', 'M', '2000-02-03', 'B', 'gfdg', 'Indiam', 'dvsd', 'davdszv')")

conn.commit()
print("Records created successfully")
conn.close()
