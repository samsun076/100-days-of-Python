# Challenge 01 from 100 days of Python.
# Taken from https://codechalleng.es/bites/7/
# Bite 07 - Parsing dates from logs.

from datetime import datetime
from datetime import timedelta

log = "day02-challenge.log"
with open (log, "r") as f:
    loglines=f.readlines()
new_list = []
shutdown = "Shutdown initiated"
for line in loglines:
    if shutdown in line:
        date_str=line.split(" ")[1]
        new_list.append((datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")))

print(new_list[1] - new_list[0])

