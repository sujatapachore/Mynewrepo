#clock pythin code
import time

while True:
    current_time = time.strftime("%H:%M:%S")  # 24-hour format
    print(current_time, end="\r")  # overwrite previous time
    time.sleep(1)
