import time
import subprocess

while True:
    f = open('loophole.txt', 'a')
    f.write(time.strftime('%m-%d-%Y %H:%M:%S')+'\n')
    f.close()

    subprocess.call("git add .", shell=True)
    subprocess.call("git commit -m timestamp", shell=True)
    subprocess.call("git push origin master", shell=True)
    time.sleep(2)
