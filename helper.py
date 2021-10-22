import os
import timeo
turnCount=0
working=1
while working:
    os.system("git add .")
    os.system("git commit -m \"auto commit to maintain focus\" ")
    os.system("git push origin master")
    time.sleep(3600)
    continue
