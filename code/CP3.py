from datetime import datetime as dt
import time as t

def timer(start):
    print(dt.now().time())
    return dt.now().time().second - start

time_start = dt.now().time().second
for i in range(5):
    t.sleep(1)
    seconds = timer(time_start)