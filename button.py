import RPi.GPIO as GPIO
from mpu6050 import mpu6050

GPIO.setmode(GPIO.BCM)

#Setup
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
ring = mpu6050(0x69)

while True:
    try:
        GPIO.wait_for_edge(19, GPIO.FALLING)
        isPressed = True
        print "STARTING BATCH"
        while isPressed:
            data = ring.get_all_data()
            accelX, accelY, accelZ = data[0]['x'], data[0]['y'], data[0]['z']
            gyroX, gyroY, gyroZ = data[1]['x'], data[1]['y'], data[1]['z']
            print "START "+str(accelX)+" "+str(accelY)+" "+str(accelZ)+" "+str(gyroX)+" "+str(gyroY)+" "+str(gyroZ)+" END"
            isPressed = not GPIO.input(19)
        print "CLOSING BATCH"
    except KeyboardInterrupt:
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
        break
GPIO.cleanup()           # clean up GPIO on normal exit
