import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

IN2 = 3
IN1 = 5
PWM = 12
STANBY = 16



GPIO.setup(IN2,GPIO.OUT)		#B-IN2
GPIO.setup(IN1,GPIO.OUT)		#B-IN1
GPIO.setup(PWM,GPIO.OUT)		#B-PWM but for test just plain output
GPIO.setup(STANBY,GPIO.OUT)		#standby

def motor_spin(clockwise):
	if clockwise:
		GPIO.output(STANBY,GPIO.HIGH)
		GPIO.output(IN1,GPIO.HIGH)
		GPIO.output(IN2,GPIO.LOW)
		GPIO.output(PWM,GPIO.HIGH)
	else:
		GPIO.output(STANBY,GPIO.HIGH)
		GPIO.output(IN1,GPIO.LOW)
		GPIO.output(IN2,GPIO.HIGH)
		GPIO.output(PWM,GPIO.HIGH)
def motor_stop():
		GPIO.output(STANBY,GPIO.LOW)
		GPIO.output(IN1,GPIO.LOW)
		GPIO.output(IN2,GPIO.LOW)
		GPIO.output(PWM,GPIO.LOW)


motor_spin(True)
sleep(3)
motor_stop()
sleep(3)
motor_spin(False)
sleep(3)
motor_stop()

GPIO.cleanup()
