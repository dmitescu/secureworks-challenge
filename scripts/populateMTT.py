import sqlite3
import random

SAMPLE_SIZE = 666
RANDOMNESS = 333

depts = ["D1", "D2", "D3", "D4"]

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()

values_mttd = []
values_mttr = []

for dep in depts:
    r = random.randint(0, RANDOMNESS)

    size = SAMPLE_SIZE + random.randint(0, RANDOMNESS)

    for i in range(0, size):
        ticket_id = random.randint(0, 4096)
        duration = random.randint(6, 360)
        values_mttd.append((ticket_id, dep, duration))

        ticket_id = random.randint(0, 4096)
        duration = random.randint(6, 360)
        values_mttr.append((ticket_id, dep, duration))
        

cursor.executemany("INSERT INTO dashboard_mttd(ticket_id, department, duration) VALUES (?, ?, ?)", values_mttd)
cursor.executemany("INSERT INTO dashboard_mttr(ticket_id, department, duration) VALUES (?, ?, ?)", values_mttr)

conn.commit()

conn.close()
