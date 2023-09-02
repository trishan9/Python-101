################################### DAY 2 PROJECT 5 - Good Morning Sir ###################################
import time
timestamp = time.strftime("%H:%M:%S")
timestamp_hour = int(time.strftime("%H"))

if(timestamp_hour >= 12 & timestamp_hour < 20):
    print(f"Good afternoon, Current Time: {timestamp}")
elif(timestamp_hour >= 20 & timestamp_hour <= 23 ):
    print(f"Good night, Current Time: {timestamp}")
else:
    print("Good morning")