#!/usr/bin/env python
import time
import os
import RPi.GPIO as GPIO

SPICLK = 7
SPIMISO = 11
SPIMOSI = 13
SPICS = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1

        # turn chip on, then off
        GPIO.output(cspin, True)
        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here

        for i in range(5):
            if (commandout & 0x80):
                GPIO.output(mosipin, True)
            else:
                GPIO.output(mosipin, False)

            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)

            commandout <<= 1

        adcout = int(0)
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
        
                if (GPIO.input(misopin)):
                        adcout |= 0x1

                adcout <<= 1

        # turn chip off
        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

def read_all():
	adcout = [0]*8
	for i in range(8):
		adcout[i] = readadc(i, SPICLK, SPIMOSI, SPIMISO, SPICS)

	return adcout
