import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self):
        # define constants
        self.INTERVAL = 1
        self.PIN = 14
        self.FREQ = 50 # Hz
        self.is_open = False
        self.OPEN_DUTY = 12.0 # +90[dec]
        self.CLOSE_DUTY = 7.25 # 0[dec]

        # setup gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN, GPIO.OUT)

        # setup pwm
        self.servo = GPIO.PWM(self.PIN, self.FREQ)

        # start pwm
        self.servo.start(0.0)

    def change_angle(self):
        if self.is_open:
            self.close()
            print("Output: close door")
        else:
            self.open()
            print("Output: open door")

        self.is_open = not self.is_open

    def open(self):
        self.servo.ChangeDutyCycle(self.OPEN_DUTY)
        time.sleep(self.INTERVAL)
        self.servo.ChangeDutyCycle(0.0)

    def close(self):
        self.servo.ChangeDutyCycle(self.CLOSE_DUTY)
        time.sleep(self.INTERVAL)
        self.servo.ChangeDutyCycle(0.0)

    def __del__(self):
        self.servo.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    servo = Servo()
    servo.change_angle()
    time.sleep(10)
    servo.change_angle()
    del servo

