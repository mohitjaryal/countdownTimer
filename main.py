# Countdown Timer using python

import time
import os  # for terminal beep on mac/linux

# User input
seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    timer = f"{mins:02d}:{secs:02d}"
    print(timer, end="\r")  # overwrite the same line
    time.sleep(1)
    seconds -= 1

# Time's up message
print("⏰ Time's up!")

# Time's up sound - macOS/Linux terminal
os.system('say "Hello sir, Time is up"')  # makes the Mac speak!
print("\a")