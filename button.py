import RPi.GPIO as GPIO
from mpu6050 import mpu6050

GPIO.setmode(GPIO.BCM)

#Setup
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
ring = mpu6050(0x69)

try:
    GPIO.wait_for_edge(19, GPIO.FALLING)
    isPressed = True
    while isPressed:
	data = ring.get_all_data()
    	isPressed = not GPIO.input(19)
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

GPIO.cleanup()           # clean up GPIO on normal exit
