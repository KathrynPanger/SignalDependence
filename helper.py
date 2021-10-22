import os
import time
turnCount=0
working=1
counter=1
while working:
    os.system("git add .")
    os.system(f"git commit -m \"dealing with time-shifting pt{counter}\"")
    os.system("git push origin master")
    time.sleep(3600)
    continue
