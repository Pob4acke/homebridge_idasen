# homebridge_idasen
Script and explanation to control an Ikea Idasen standing desk with Apple home

## Important note
No further development on this, as there is a proper homebridge plugin now: [homebridge-linak](https://github.com/vniehues/homebridge-linak)

## Set up

### Prerequisites

- Ikea Idasen standing desk
- [Homebridge](https://homebridge.io) installation on a device that has bluetooth

### Install

1. Install [idasen-controller](https://github.com/rhyst/idasen-controller) and [homebridge-blinds-cmd](https://github.com/hjdhjd/homebridge-blinds-cmd) first
2. Make sure the homebridge device is paired to the desk over bluetooth
3. copy the script "move.py" on somewhere to your homebridge device
4. python2 and python3 need to be installed. Python2 for this script and 3 for idasen-controller (I was having issues with my code in python3)

### Configuration

1. in the homebridge configuration for "blinds-cmd" enter your favourite name and change the value of the "Up Command" and "Down Command Script" to:
```
python2 [path_to_skript]/move.py
```

## Features
Ads the standing desk as a controllable blind to the home app. You can then move that blind up and down and and so the desk will do.
Unfortinatly there is nothing like a desk or similar in homekit, so this might be the best solution to freely adjust the height.

I would recomment to set some home scenes for your standing and sitting height, with your prefered value, e.g.:
Standing: blind 90% open
Sitting: blind 15% open
With that you can even say something like "Move desk to sitting height." to Siri.

## How it works
The script is rather easy (as you might see). Once a height is adjusted in homekit the plugin "homebridge-blinds-cmd" executes the python script "move.py" with a percantage value for the height as an argument. The python script calculates a height from the input value with the following function:
```
y = 620 + (x / 100) * 650
```
620mm is the minimum height of the desk and the maximum will be 1270mm. So with this calculation the percantage that comes from the homebridge plugin will be set to a proper height value for the desk. You will also have the full adjustment range of the desk in homekit.

Next the height value is send to the desk using "idasen-controller --move-to" command.
As "idasen-controller" delivers many outputs on the screen (which is good for debuggign!), this needs to be supressed for the homebridge plugin. The homebridge plugin just wants a percentage value for the height as a response. Therefore the final height value from "idasen-controller" will be taken and calulcated back to a percentage value with the reverse function:
```
x = y/6,5 - 95
```
As an int value is expected from the homebridge plugin, this calculation is fine.

## ToDo
### check script for python3
check why it does not work in python 3
### status script
As there is no status script, to check the height frequently this needs to be done
--> Done by vniehues, check out [homebridge-linak](https://github.com/vniehues/homebridge-linak)
### stop script
to stop the last command a script needs to be created
### create own homebridge plugin
To create an own homebridge plugin should be the final step
--> Done by vniehues, check out [homebridge-linak](https://github.com/vniehues/homebridge-linak)

## Notes
Special thanks to [idasen-controller](https://github.com/rhyst/idasen-controller) and [homebridge-blinds-cmd](https://github.com/hjdhjd/homebridge-blinds-cmd) as those are the basis for my small script.
If you are willing to contribute, feel free to improve my solution! There are many things one can do better, as I'm just a beginner :)

And for sure thanks to the one who made it better than me: vniehues, check out [homebridge-linak](https://github.com/vniehues/homebridge-linak)
