# WebDVM

A low-cost Digital Volt-Meter (DVM) using an Arduino and Raspberry Pi zero
with a browser interface.

You can find websocketd [here](https://github.com/joewalnes/websocketd).
Yiou can download the latest release [here](https://github.com/joewalnes/websocketd/releases)

I've described the project in a series of three blog posts. Start
[here](https://blog.rareschool.com/2019/06/build-web-based-dvm-using-arduino-and.html).


## Hardware required

1. An Arduino Uno. (Other models would work; I've tested it with a Nano.)
1. A Raspberry Pi zero W or a full-size Pi, with Raspbian Stretch and WiFi set up
or a wired (Ethernet) connection.
1. A cable or cables to connect the Arduino to the USB port on the Pi.
1. A power source for the Pi and a cable to connect it.
1. A computer with a browser connected to the same network as the Pi.

## Installation

1. On the Arduino, install dvm.ino from this repository
1. On the Pi, 
    1. Download the zip file from GitHub.
    
        `wget https://github.com/romilly/WebDVM/archive/master.zip`
    1. Unzip it: `unzip master.zip`
    1. Change to the newly created directory: `cd WebDVM-master`
    1. If you've changed the Raspberry Pi's hostname, edit `index.html` 
    to reflect the current hostname.
    1. Run `./websocketd --port=8080 --staticdir=. ./read-dvm.py`
1. In your browser, open `raspberrypi:8080` (or use whatever hostname you chose for the Pi)


Have fun!

If you hit problems, please raise an issue on GitHub.

If you have questions, I'm [@rareblog](https://twitter.com/rareblog) on Twitter.

