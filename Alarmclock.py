import datetime
import time
import winsound

alarm_time = input("Enter the alarm time (HH:MM): ")

alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
alarm_time = datetime.datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)

while True:

    now = datetime.datetime.now()
    
    if now >= alarm_time:
        print("Time to Wake up!")
        winsound.Beep(1000,1000)
        break
    
    time.sleep(10)  

