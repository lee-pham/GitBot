import time
import subprocess

while True:

    f = open('loophole.txt', 'a')
    f.write(time.strftime('%m-%d-%Y %H:%M:%S')+'\n')
    f.close()

    subprocess.call(“git add -A”)
    subprocess.call(“git commit -m ‘add timestamp’”)
    subprocess.call(“git push origin master”)
    time.sleep(10)