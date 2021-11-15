import os
import time
turnCount=0
working=1
counter=1
while working:
    os.system("git add .")
    os.system(f"git commit -m \"machine learning pt {counter}\"")
    os.system("git push origin master")
    time.sleep(2000)
    continue
