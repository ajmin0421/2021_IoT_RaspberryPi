import RPi.GPIO as GPIO
import time

RED_PIN = 4
YELLOW_PIN = 5
GREEN_PIN = 6
RSWITCH_PIN = 9
YSWITCH_PIN = 10
GSWITCH_PIN = 11

GPIO.setmode(GPIO.BCM) 
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(RSWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(YSWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GSWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  

try:
  while True:
    Rval = GPIO.input(RSWITCH_PIN)
    Yval = GPIO.input(YSWITCH_PIN)
    Gval = GPIO.input(GSWITCH_PIN)
    print(Rval,Yval,Gval)
    GPIO.output(RED_PIN, Rval)
    GPIO.output(YELLOW_PIN, Yval)
    GPIO.output(GREEN_PIN, Gval)

finally:
  GPIO.cleanup()
  print('cleanup and exit')

  