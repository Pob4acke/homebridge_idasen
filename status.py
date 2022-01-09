import sys
import subprocess
import time

### call idasen-controler to check current height and then kill the subprocess
cmd = subprocess.Popen("/home/pi/.local/bin/idasen-controller --monitor", shell=True, stdout=subprocess.PIPE)
time.sleep(10)
cmd.kill()


print(cmd.stdout)
### calc height to percantage value as return
for line in cmd.stdout:
        print(line)
        if "Height: " in line: # excample line in output from idasen-controler "Height:  761mm Speed:  0mm/s"
                print(line)     
                height_str = line[8:].split("m")[0] #remove first 8 chars and use the string till first "m" --> the acutal height in mm
                height = int(height_str)
                height_rel = float(height)/6.5 - 95
                height_rel = int(height_rel)
                print(height_rel)



