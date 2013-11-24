import servo

def set_motor(motor, speed):
    (pos, neg) = motor
    servo.setMotorSpeed(neg, pos, speed)

def stop_motor(motor):
    (pos, neg) = motor
    servo.setMotorSpeed(neg, pos, 0)