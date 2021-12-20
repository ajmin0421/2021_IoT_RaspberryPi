import RPi.GPIO as GPIO
import time

LED_red_PIN = 4
LED_yellow_PIN = 17
LED_green_PIN = 27
GPIO.setmode(GPIO.BCM) #GPIO.BOARD
GPIO.setup(LED_red_PIN, GPIO.OUT) #GPIO.IN
GPIO.setup(LED_yellow_PIN, GPIO.OUT) #GPIO.IN
GPIO.setup(LED_green_PIN, GPIO.OUT) #GPIO.IN

GPIO.output(LED_red_PIN, GPIO.HIGH) #1, TRUE
print("red on")
time.sleep(2)
GPIO.output(LED_red_PIN, GPIO.LOW)


GPIO.output(LED_yellow_PIN, GPIO.HIGH) #1, TRUE
print("yellow on")
time.sleep(2)
GPIO.output(LED_yellow_PIN, GPIO.LOW)


GPIO.output(LED_green_PIN, GPIO.HIGH) #1, TRUE
print("green on")
time.sleep(2)
GPIO.output(LED_green_PIN, GPIO.LOW)



GPIO.cleanup() #GPIO 핀 상태 초기화