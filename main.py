# Countdown Timer using python

import time

# User input
second = int(input('Enter seconds :'))

# Main logic
while second > 0:
    mins = second / 60
    sec = second % 60
    timer = f"{mins:02d}:{sec:02d}"
    print(timer, end="\r")