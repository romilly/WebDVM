# WebDVM

A low-cost Digital Volt-Meter (DVM) using an Arduino and Raspberry Pi zero
with a browser interface.

I'll be describing the project in a series of blog posts shortly.

Meanwhile, here are minimalist instructions:

## Hardware required

1. An Arduino Uno (other models would also work).
1. A Raspberry Pi zero W or a full-size Pi, with Raspbian Stretch and WiFi set up
or a wired (Ethernet) connection.
1. A cable or cables to connect the Arduino to the USB port on the Pi.
1. A power source for the Pi and a cable to connect it.
1. A computer with a browser on the same network as the Pi.

## Installation

1. On the Arduino, install dvm.ion from this repository
1. On the Pi, 
    1. set the Pi's hostname to `dvm`, or edit `index.html` 
    to reflect the current hostname.
    1. create a new directory somewhere - `dvm`, for instance.
    1. change to that directory.
    1. Use wget to download read-dev.md and index.html.
    1. Install [websocketd](http://websocketd.com/). (Make sure you get the ARM version!)
    1. Run `websocketd --port=8080 --staticdir=. ./read-dvm.py`
1. In your browser, open dvm:8080 (or whatever hostname you chose for the Pi)




