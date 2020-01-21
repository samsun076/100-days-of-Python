number = list(range(1,10))
number

import itertools
import sys
import time


symbols = itertools.cycle('-\|/')
cycles = 0

# removes the while True and added a counter
while cycles < 100:
    sys.stdout.write('\r' + next(symbols))
    sys.stdout.flush()  #forces what ever going to stdout onto the screen.  Sometimes it goues to a buffer
    time.sleep(.1)
    cycles += 1
