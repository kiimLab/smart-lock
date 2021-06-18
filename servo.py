import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, interval=1, pin=14, freq=50, open_duty=12.0, close_duty=7.25):
        # define constants
        self.INTERVAL = interval
        self.PIN = pin
        self.FREQ = freq # Hz
        self.OPEN_DUTY = open_duty # +90[dec]
        self.CLOSE_DUTY = close_duty # 0[dec]

        # init internal state
        self.is_open = False

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

