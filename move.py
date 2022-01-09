import sys
import subprocess

### calc percentage to height
height_rel = sys.argv[1]
height = 620 + float(height_rel)/100*650
height = int(height)
if height == 620:
        height = 621 #in some cases idasen-control gets an exception when moving to lowest position (due to some overdirve?)

### call idasen-controler with height
cmd = subprocess.Popen("/home/pi/.local/bin/idasen-controller --move-to " + str(height), shell=True, stdout=subprocess.PIPE)

### calc new height back to percantage value as return
for line in cmd.stdout:
        if "Final height: " in line: # excample line in output from idasen-controler "Final height:  750mm (Target:  750mm)"
                height_str = line[14:].split("m")[0] #remove first 14 chars and use the string till first "m" --> the acutal height in mm
                height = int(height_str)
                height_rel = float(height)/6.5 - 95
                height_rel = int(height_rel)
                print(height_rel) 
