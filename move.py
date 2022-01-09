import sys
import os

height_rel = sys.argv[1]
height = height_rel
height = 620 + float(height)/100*650
height = int(height)
print(height_rel) #output for homekit plugin

os.popen('/home/pi/.local/bin/idasen-controller --move-to ' + str(height) + " > /dev/null")
