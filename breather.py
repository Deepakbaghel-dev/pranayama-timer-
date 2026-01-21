import time
import winsound

def countdown(x): # Countdown timer that beeps when phase completes
    while x:
        mins, secs = divmod(x, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        x -= 1
    winsound.Beep(528, 2000) 

inhale_time = 4    
hold_time= 8
exhale_time = 4
pause_time = 4

y=int(input("Enter no of times loop continue: "))
count = 0
for z in range(y):
    count+=1
    print(count)
    countdown(int(inhale_time))
    countdown(int(hold_time))
    countdown(int(exhale_time))
    countdown(int(pause_time))
