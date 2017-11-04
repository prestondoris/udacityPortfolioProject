import webbrowser
import time

total_breaks = 5
count = 0
print("The program was started on " +time.ctime())
while(count < total_breaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=Z3ZAGBL6UBA")
    count += 1

