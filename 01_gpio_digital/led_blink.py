import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM) #GPIO.BOARD
GPIO.setup(LED_PIN, GPIO.OUT) #GPIO.IN

for i in range(10):
    GPIO.output(LED_PIN, GPIO.HIGH) #1, TRUE
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN, GPIO.LOW)
    print("led off")
    time.sleep(2)

GPIO.cleanup() #GPIO 핀 상태 초기화