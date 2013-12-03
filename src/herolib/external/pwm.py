#!/usr/bin/python

import time
import math
from Adafruit_I2C import Adafruit_I2C

# ============================================================================
# PCA9635 16-Channel PWM IC
# ============================================================================

class PWM :
  # Registers/etc.
  __MODE1              = 0x00
  __LED0               = 0x02

  def __init__(self, address=0x40, debug=False):
    self.i2c = Adafruit_I2C(address)
    self.address = address
    self.debug = debug
    if (self.debug):
      print "Reseting PCA9685"
    self.i2c.write8(self.__MODE1, 0x00)

  # def setPWMFreq(self, freq):
  #   oldmode = self.i2c.readU8(self.__MODE1);
  #   newmode = (oldmode & 0x7F) | 0x10             # sleep
  #   self.i2c.write8(self.__MODE1, newmode)        # go to sleep
  #   self.i2c.write8(self.__PRESCALE, int(math.floor(prescale)))
  #   self.i2c.write8(self.__MODE1, oldmode)
  #   time.sleep(0.005)
  #   self.i2c.write8(self.__MODE1, oldmode | 0x80)

  def setPWM(self, ledno, freq):
    # write 0x02+ledno
    self.i2c.write8(self.__LED0+ledno, freq)



