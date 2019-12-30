# Pybites Challenege to use Datetime for own problem
# I decided to take the uptime command from the MacOs
# and calculate the date it was last reboot


from datetime import datetime
from datetime import date
from datetime import timedelta
import shlex
import subprocess


cmd = "uptime"
arg = shlex.split(cmd)

p = subprocess.Popen(arg, stdout=subprocess.PIPE)
uptime_output = p.communicate()
days_up = int(uptime_output[0].split()[2])

today = date.today()
last_boot = timedelta(days = days_up)

print("Days your MacOS has been up: ", days_up, "\nIt was last reboot: ", today - last_boot)

