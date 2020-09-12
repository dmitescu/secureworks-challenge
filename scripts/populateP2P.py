import sqlite3
import random
import time

from datetime import datetime

def str_time_prop(start, end, prop):
    ptime = start + prop * (end - start)

    return ptime

def random_date(start, end, prop):
    return str_time_prop(start, end, prop)

SAMPLE_SIZE = 6666

FORMAT = '%m/%d/%Y %I:%M %p'

START_DATE = time.mktime(time.strptime("1/1/2015 1:00 AM", FORMAT))
END_DATE1 = time.mktime(time.strptime("1/1/2020 1:00 AM", FORMAT))
END_DATE2 = time.mktime(time.strptime("1/5/2017 1:00 AM", FORMAT))
END_DATE3 = time.mktime(time.strptime("1/12/2015 1:00 AM", FORMAT))

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()

values = []

for i in range(0, int(SAMPLE_SIZE/3)):
    date = datetime.fromtimestamp(random_date(START_DATE, END_DATE1, random.random()))
    values.append((date,))

    
for i in range(0, int(SAMPLE_SIZE/3)):
    date = datetime.fromtimestamp(random_date(START_DATE, END_DATE2, random.random()))
    values.append((date,))


for i in range(0, int(SAMPLE_SIZE/3)):
    date = datetime.fromtimestamp(random_date(END_DATE2, END_DATE1, random.random()))
    values.append((date,))

r = cursor.executemany("INSERT INTO dashboard_p2ppacket(date) VALUES (?)", values)

conn.commit()

conn.close()
