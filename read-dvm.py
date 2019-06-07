#! /usr/bin/python3

import serial
import io
import sys
from serial.tools import list_ports

TIMEOUT_SECONDS = 1

devices = [port.device for port in list_ports.comports()]
ports = [port for port in devices if port in ['/dev/ttyACM0','/dev/ttyUSB0']]
if len(ports) != 1:
    raise Exception('cannot identify port to use')
port = ports[0]

with serial.Serial(port, 9600, timeout=TIMEOUT_SECONDS) as ser:
    # We use a Bi-directional BufferedRWPair so people who copy + adapt can write as well as read
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
    while True:
        try:
            line = sio.readline()
        except UnicodeDecodeError:
            continue # decode error - keep calm and carry on
        if len(line) == 0: # EOF
            break
        print(line)
        sys.stdout.flush() # to avoid buffering, needed for websocketd
