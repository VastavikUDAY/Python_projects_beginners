import time
import webbrowser
import random


print ("What time do you want to wake up?")
print ("Use this form.\nExample: 06:30:00")
Alarm = input("> ")



time = time.strftime("%H:%M:%S")



while time != Alarm:
    print ("The time is" + Time)
    Time = time.strftime("%H:%M:%S")
    time.sleep(1)
    
    
    
if Time == Alarm:
    print ("Time to wake up!")
