import glob
import time
import subprocess as sp

while True:
    try:
        out = sp.check_output("git pull", shell=True)
    except sp.CalledProcessError:
        out = "Git pull failed"
    files = glob.glob("./*")
    if "Already up-to-date" not in out:
        print("Git output = ", out)
    for f in files:
        if "py" not in f and ".md" not in f:
            try:
                with open(f,'r') as h:
                    print("Filename is " + f 
                          + " containing: " 
                         + h.read().replace("\n",""))
            except IOError:
                print(f + " not found")


    time.sleep(20.)

    
