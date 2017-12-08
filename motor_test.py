import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BOARD)

IN2 = 3
IN1 = 5
PWM = 12
STANBY = 16



GPIO.setup(IN2,GPIO.OUT)		#B-IN2
GPIO.setup(IN1,GPIO.OUT)		#B-IN1
GPIO.setup(PWM,GPIO.OUT)		#B-PWM
pwm_out = GPIO.PWM(PWM,100)		#pwm class setup as pwm_out
pwm_out.start(0)
GPIO.setup(STANBY,GPIO.OUT)		#standby

def motor_spin(clockwise,duty_cycle):
	if clockwise:
		GPIO.output(STANBY,GPIO.HIGH)
		GPIO.output(IN1,GPIO.HIGH)
		GPIO.output(IN2,GPIO.LOW)
		pwm_out.ChangeDutyCycle(duty_cycle)
	else:
		GPIO.output(STANBY,GPIO.HIGH)
		GPIO.output(IN1,GPIO.LOW)
		GPIO.output(IN2,GPIO.HIGH)
		pwm_out.ChangeDutyCycle(duty_cycle)
def motor_stop():
		GPIO.output(STANBY,GPIO.LOW)
		GPIO.output(IN1,GPIO.LOW)
		GPIO.output(IN2,GPIO.LOW)
try:
	motor_stop()
	print(' Use simple commands to test your motor: \n C = clockwise \n A or AC = anit-colckwise \n S = stop \n Then add a speed(0-255) \n an example: \n "C-200" \n "S-0" \n you can exit anytime with ^C \n')

	while True:
		usr_sig = raw_input('Input>')
		direction,speed = usr_sig.split('-')
		print('PLACE:split')
		speed = int(speed)
		if speed > 255:
			speed = 255
		DC = speed/2.55
		print('PLACE:if statement')
		if direction == 'C':
			motor_spin(True,DC)
			print('PLACE:motor spin')
		elif direction == 'A' or direction == 'AC':
			motor_spin(False,DC)
			print('PLACE:motor spin')
		elif direction == 'S':
			motor_stop()
			print('PLACE:motor stop')

except:
	print(sys.exc_info())
	print('\nGoodBye	\n')
	pwm_out.stop()
	GPIO.cleanup()

