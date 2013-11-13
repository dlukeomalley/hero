import RPi.GPIO as GPIO
import mpr121
import time

CAPSENSE_IRQ_PIN = 8
NUM_TOUCH_PADS = 12
MPR121_ADDR = 0x5a

# Initialize GPIO Pin numbering and I/O
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CAPSENSE_IRQ_PIN, GPIO.IN)

# Initialize MP121 capacitive touch board
mpr121.TOU_THRESH = 0x15
mpr121.REL_THRESH = 0x12
mpr121.setup(MPR121_ADDR)

# Loop
while True:
    sensor = [0] * NUM_TOUCH_PADS
    touch_data = mpr121.readData(MPR121_ADDR)

    #print bin(touch_data)

    for i in range(NUM_TOUCH_PADS):
        if touch_data & (1 << i):
            sensor[i] = 1

    print sensor
    time.sleep(.5)
