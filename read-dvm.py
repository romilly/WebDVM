#! /usr/bin/python3

import serial
import io
import sys

TIMEOUT_SECONDS = 1

with serial.Serial('/dev/ttyACM0', 9600, timeout=TIMEOUT_SECONDS) as ser:
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
