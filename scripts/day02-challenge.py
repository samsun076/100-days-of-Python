# Challenge 01 from 100 days of Python.
# Taken from https://codechalleng.es/bites/7/
# Bite 07 - Parsing dates from logs.

from datetime import datetime
from datetime import timedelta

log = "day02-challenge.log"
with open (log, "r") as f:
    loglines=f.readlines()

####################################
# Basic script not using functions #
####################################

new_list = []
SHUTDOWN_EVENT = "Shutdown initiated"
for line in loglines:
    if SHUTDOWN_EVENT in line:
        date_str=line.split(" ")[1]
        new_list.append((datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")))

print(new_list[1] - new_list[0])
print("")

###################
# Using Functions #
###################


#def convert_to_datetime_01(line):
#    datestring=line.split()[1]
#    return datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S")

#def time_between_shutdowns_01(loglines):
#    newer_list= []
#    for line in loglines:
#        if SHUTDOWN_EVENT in line:
#            newer_list.append(convert_to_datetime_01(line))
#    return max(newer_list) - min(newer_list)


#print(time_between_shutdowns_01(loglines))
#print("")



############################################
# Solution from PyBites with comprehension #
# lists, better variable naming, etc       #
############################################

def convert_to_time(lines):
    timestamp = line.split()[1]
    date_str = '%Y-%m-%dT%H:%M:%S'
    print("timestamp is ", timestamp)
    return datetime.strptime(timestamp, date_str)



def time_between_shutdowns(loglines):
    shutdown_entries=[line for line in loglines if SHUTDOWN_EVENT in line]
    print(shutdown_entries)
    shutdown_times=[convert_to_time(event) for event in shutdown_entries]
    print(shutdown_times)
    return max(shutdown_times) - min(shutdown_times)


print(time_between_shutdowns(loglines))







