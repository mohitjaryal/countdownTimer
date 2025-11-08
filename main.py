# Countdown Timer using python

import time

# User input
seconds = int(input('Enter seconds :'))

# Main logic
while seconds > 0:
    mins = seconds / 60
    sec = seconds % 60
    timer = f"{mins:02d}:{sec:02d}"
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1
    
print("⏰ Time's up!")