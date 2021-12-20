from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN1 = 2


# Flask 객체 생성
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)

#alt shift 밑에 화살표 = 복붙
# 0.0.0.0:5000/
@app.route("/")
def home():
    return render_template("led.html")
        

@app.route("/<color>/<op>")   
def led_op(color, op):
        if op == "on":
            GPIO.output(LED_PIN1, GPIO.HIGH)
            return "LED ON"
        
        elif op == "off":
            GPIO.output(LED_PIN1, GPIO.LOW)
            return "LED OFF"

        else:
            return "ERROR"
    #elif color == "Bule":
        if op == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return'''
            <p>Led Yel on</p>
            <a href="/">Go Home</a>
        '''
        elif op == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return'''
            <p>Led Yel off</p>
            <a href="/">Go Home</a>
        '''


#터미널에서 직접 실행시킨 경우 
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    finally:
        GPIO.cleanup()