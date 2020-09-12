import sqlite3
import random

SAMPLE_SIZE = 666
RANDOMNESS = 666

subnets  = ["S1", "S2", "S3", "S4"]

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()

values = []

for sub in subnets:
    r = random.randint(0, RANDOMNESS)

    size = SAMPLE_SIZE + random.randint(0, RANDOMNESS)

    for i in range(0, size):
        ticket_id = random.randint(0, 4096)
        values.append(("H", sub))

    
    size = SAMPLE_SIZE + random.randint(0, RANDOMNESS)
    
    for i in range(0, size):
        ticket_id = random.randint(0, 4096)
        values.append(("Q", sub))
        
cursor.executemany("INSERT INTO dashboard_intrusionattempt(intrusion_type, subnet) VALUES (?, ?)", values)

conn.commit()

conn.close()
