#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time
import numpy as np

NODE=0 
NET=0
KEY="1234567891011121"
TIMEOUT=3
TOSLEEP=0.1

# Defaults:         freqBand,    nodeID, networkID, isRFM69HW = True, intPin = 18, rstPin = 22, spiBus = 0, spiDevice = 0
radio = RFM69.RFM69(RF69_433MHZ, NODE,   NET,       True)
print "class initialized"

print "reading all registers"
results = radio.readAllRegs()
#for result in results:
    print result

print "Performing rcCalibration"
radio.rcCalibration()

print "setting high power"
radio.setHighPower(True)

print "Checking temperature"
print radio.readTemperature(0)

#print "setting encryption"
#radio.encrypt(KEY)

print "starting loop..."
sequence = 0
while True:

    msg = "I'm radio %d: %d" % (NODE, sequence)
    sequence = sequence + 1

    print "tx to radio 2: " + msg
    if radio.sendWithRetry(2, msg, 3, 20):
        print "ack recieved"

    print "start recv..."
    radio.receiveBegin()
    timedOut=0
    while not radio.receiveDone():
        timedOut+=TOSLEEP
        time.sleep(TOSLEEP)
	if timedOut > TIMEOUT:
            print "timed out waiting for recv"
            break

    print "end recv..."
    #print " *** %s from %s RSSI:%s" % ("".join([chr(letter) for letter in radio.DATA]), radio.SENDERID, radio.RSSI)
    # >>> a.astype(np.uint8).data.hex()    
    print "Received data in HEX: %s" % (radio.DATA.astype(np.uint8).data.hex())
    if radio.ACKRequested():
        print "sending ack..."
        radio.sendACK()
    else:
        print "ack not requested..."

print "shutting down"
radio.shutdown()
