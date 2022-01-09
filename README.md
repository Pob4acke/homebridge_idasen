# homebridge_idasen
Script and explanation to control an Ikea Idasen standing desk with Apple home

## Set up

### Prerequisites

- Ikea Idasen standing desk
- [Homebridge](https://homebridge.io) installation on a device that has bluetooth

### Install

1. Install [idasen-controller](https://github.com/rhyst/idasen-controller) and [homebridge-blinds-cmd](https://github.com/hjdhjd/homebridge-blinds-cmd) first
2. Make sure the homebridge device is paired to the desk over bluetooth
3. copy the script "move.py" on somewhere to your homebridge device

### Configuration

1. in the homebridge configuration for "blinds-cmd" enter your favourite name and change the value of the "Up Command" and "Down Command Script" to:
```
python3 [path_to_skript]/move.py
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
As "idasen-controller" delivers many outputs on the screen (which is good for debuggign!), this needs to be supressed for the homebridge plugin. The plugin just wants a percentage value for the height as a response. So for that at the moment I just return the  input value (as print()).

## ToDo
### improve return value handling

The actual return value should be taken from height that comes from idasen-controller. With that it should be possible to indicate if the desk got stuck in between

### status script

As there is no status script, to check the height frequently this needs to be done

### stop script

to stop the last command a script needs to be created

## Notes
Special thanks to [idasen-controller](https://github.com/rhyst/idasen-controller) and [homebridge-blinds-cmd](https://github.com/hjdhjd/homebridge-blinds-cmd) as those are the basis for my small script.
If you are willing to contribute, feel free to improve my solution! There are many things one can do better, as I'm just a beginner :)
