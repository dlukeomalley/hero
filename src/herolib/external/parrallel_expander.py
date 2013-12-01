#!/usr/bin/env python
# MCP23017 Code
# Reference: http://ww1.microchip.com/downloads/en/DeviceDoc/21952b.pdf

import smbus
bus = smbus.SMBus(1)

# Register Addresses
IODIRA = 0x00
IPOLA = 0x01
GPINTENA = 0x02
DEFVALA = 0x03
INTCONA = 0x04
GPPUA = 0x06
INTFA = 0x07
INTCAPA = 0x08
GPIOA = 0x09
OLATA = 0x0A

IOCON = 0x05

IODIRB = 0x10
IPOLB = 0x11
GPINTENB = 0x12
DEFVALB = 0x13
INTCONB = 0x14
GPPUB = 0x16
INTFB = 0x17
INTCAPB = 0x18
GPIOB = 0x19
OLATB = 0x1A

ADDR = 0x20

def setup():
	# Reset the chip
	GPIO.output(RESET, False)
	GPIO.output(RESET, True)

	# BANK = 1
	# MIRROR = 1 (both ints tied together)
	# SEQOP = 1, want to specify what we read from
	# DISSLW = 0 is default
	# HAEN = 0, A2 = A1 = A0
	# rest are default values
	control = 0b11100000
	bus.write_byte_data(ADDR, IOCON, control)

	# Set GPIOA to input, GPIOB to output
	bus.write_byte_data(ADDR, IODIRA, 0xFF)
	bus.write_byte_data(ADDR, IODIRB, 0x00)

	# Enable interrupt-on-change
	bus.write_byte_data(ADDR, GPINTENA, 0xFF)
	bus.write_byte_data(ADDR, GPINTENB, 0x00)

	# Interrupts when pin input != to DEFVAL
	bus.write_byte_data(ADDR, INTCONA, 0xFF)
	bus.write_byte_data(ADDR, INTCONB, 0x00)

	# Default value to compare inputs to for interrupts
	bus.write_byte_data(ADDR, DEFVALA, 0x00)

	# Pull up output on GPIOB
	bus.write_byte_data(ADDR, GPPUA, 0x00)
	bus.write_byte_data(ADDR, GPPUB, 0XFF)

def readData(side, pin):
	# TODO, make this channel and side
	return (bus.read_byte_data(ADDR, GPIOA) | pin) > 0

def writeData(val):
	bus.write_byte_data(ADDR, GPIOB, val)

setup()
for i in range(10):
	writeData(0)
	time.sleep(.5)
	writeData(0xFF)
	time.sleep(.5)
