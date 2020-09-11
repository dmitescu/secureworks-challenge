import sqlite3
import random
import time

from datetime import datetime

def str_time_prop(start, end, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

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
    uid = random.randint(1, 1024)
    date = datetime.fromtimestamp(random_date(START_DATE, END_DATE1, random.random()))
    duration = random.randint(1,4)

    values.append((uid, date, duration))

    
for i in range(0, int(SAMPLE_SIZE/5)):
    uid = random.randint(1, 1024)
    date = datetime.fromtimestamp(random_date(START_DATE, END_DATE2, random.random()))
    duration = random.randint(1,4)

    values.append((uid, date, duration))


for i in range(0, int(SAMPLE_SIZE/7)):
    uid = random.randint(1, 1024)
    date = datetime.fromtimestamp(random_date(START_DATE, END_DATE2, random.random()))
    duration = random.randint(1,4)

    values.append((uid, date, duration))

r = cursor.executemany("INSERT INTO dashboard_downtime(deployment_id, date, duration) VALUES (?, ?, ?)", values)

conn.commit()

conn.close()
