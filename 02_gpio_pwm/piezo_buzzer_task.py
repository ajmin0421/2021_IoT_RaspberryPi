import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#주파수 : 도(262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)
melody = [262,294,330,349,392,440,494,523] 

do = melody[0] 
re = melody[1]
mi = melody[2]
pa = melody[3]
sol = melody[4]
ra = melody[5]
ci = melody[6]
ldo = melody[7]
sound = [sol,sol,ra,ra,sol,sol,mi,-1,sol,sol,mi,mi,re,-1,-1,sol,sol,ra,ra,sol,sol,mi,-1,sol,mi,re,mi,do-1,-1,]

beat = [1,1,1,1,1,1,2,1,1,1,1,4,1,1,1,1,1,1,2,1,1,1,1,4]

try:
    for i in sound:
        if i!=-1:
            pwm.ChangeFrequency(i)
            time.sleep(0.5)
        if i==-1:
            time.sleep(0.5)


finally:
    pwm.stop()
    GPIO.cleanup()