from ..thirdparty.Adafruit_I2C import Adafruit_I2C

# Initialise the PWM device using the default address

ADDR = 0x00
MODE1 = 0x00
LED0 = 0X02
LED_BANK1 = 0x014

pwm = Adafruit_I2C(ADDR)
pwm.write8(MODE1, 0x01) # turn on chip, set ALLCALL

# LED Mode for ind. PWM control
for i in range(4):
    pwm.write8(LED_BANK1 + i, 0xAA)

def setMotorSpeed(pos, neg, speed):
    pos_speed = 0
    neg_speed = 0

    # ensure abs(speed) is never greater than 1
    if speed > 1:
        speed = 1
    elif speed < -1:
        speed = -1

    if speed >= 0:
        pos_speed = int(speed*0xFF)
    else:
        neg_speed = int(-speed*0xFF)

    pwm.write8(LED0 + pos, pos_speed)
    pwm.write8(LED0 + neg, neg_speed)
