import RPi.GPIO as GPIO
import time
#BUZZER의 pin 설정
BUZZER_PIN = 26;
#button pin 설정
LB_PIN=14;#시작하는 버튼
RB_PIN=15;#시간을 올리는 버튼
# GPIO 7개 pin 번호 설정
SEGMENT_PINS=[21,20,5,6,7,24,23]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)
GPIO.setup(LB_PIN,GPIO.OUT)
GPIO.setup(RB_PIN,GPIO.OUT)

for segment in SEGMENT_PINS:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.setup(segment,GPIO.LOW)

pwm = GPIO.PWM(BUZZER_PIN,262)

Ndata = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9
val = 0

try:
    while True:
        #버튼으로 시간 조작
        if GPIO.input(RB_PIN) == GPIO.HIGH:
            val+=1
        if val==10:
            val-=1
            break
        print(val)
        #7세그먼트 숫자 표시
        for i in range(len(SEGMENT_PINS)):
            GPIO.output(SEGMENT_PINS[i],Ndata[val][i])    
        if GPIO.input(LB_PIN)==GPIO.HIGH:
            break
        time.sleep(0.1)

    while True:
        for i in range(val):
            time.sleep(1)#원래는 1분 단위여서 60을 적어야되지만 지금은 실행 영상 때문에 1초 단위로 바꿈
            #7세그먼트 숫자 표시
            for j in range(len(SEGMENT_PINS)):
                GPIO.output(SEGMENT_PINS[j],Ndata[val-i][j])    
        #부져 껐다 키기
        pwm.start(50)
        time.sleep(2)
        pwm.stop()
        break
finally:
    GPIO.cleanup()
    print('cleanup and exit')
        

