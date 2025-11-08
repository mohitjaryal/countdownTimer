# Countdown Timer using python

import time

# User input
second = int(input('Enter seconds :'))

# Main logic
while second > 0:
    mins = second / 60
    sec = second % 60