secs = 10000
hrs = int(secs / 3600)
secsLeft = secs % 3600
Mins = int(secsLeft/60)
seconds = secsLeft%60
milliSecs = secsLeft%120

print("Lab03, 80 Point Version")
print("Starting seconds: ", secs)
print("Hours: ", hrs)
print("Minutes: ", Mins)
print("Seconds: ", seconds)
print("Milliseconds: ", milliSecs)

