import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BOARD)

AIN2 = 3
AIN1 = 5
BIN2 = 11
BIN1 = 13
CIN2 = 18
CIN1 = 22

PWM = 12
STANBY = 16

GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(CIN2,GPIO.OUT)
GPIO.setup(CIN1,GPIO.OUT)

GPIO.setup(STANBY,GPIO.OUT)
GPIO.setup(PWM,GPIO.OUT)
pwm_out = GPIO.PWM(PWM,100)		#pwm class setup as pwm_out
pwm_out.start(0)

def motor_spin(motor,clockwise,duty_cycle):
	GPIO.output(STANBY,GPIO.HIGH)

	if motor == 'A':
		if clockwise:
			GPIO.output(AIN1,GPIO.HIGH)
			GPIO.output(AIN2,GPIO.LOW)
			pwm_out.ChangeDutyCycle(duty_cycle)
		else:
			GPIO.output(AIN1,GPIO.LOW)
			GPIO.output(AIN2,GPIO.HIGH)
			pwm_out.ChangeDutyCycle(duty_cycle)

	elif motor == 'B':
		if clockwise:
			GPIO.output(BIN1,GPIO.HIGH)
			GPIO.output(BIN2,GPIO.LOW)
			pwm_out.ChangeDutyCycle(duty_cycle)
		else:
			GPIO.output(BIN1,GPIO.LOW)
			GPIO.output(BIN2,GPIO.HIGH)
			pwm_out.ChangeDutyCycle(duty_cycle)

	elif motor == 'C':
		if clockwise:
			GPIO.output(CIN1,GPIO.HIGH)
			GPIO.output(CIN2,GPIO.LOW)
			pwm_out.ChangeDutyCycle(duty_cycle)
		else:
			GPIO.output(CIN1,GPIO.LOW)
			GPIO.output(CIN2,GPIO.HIGH)
			pwm_out.ChangeDutyCycle(duty_cycle)

	else:
		print('ERROR: No motor called ',str(motor),' !')




def motor_stop(motor):
	if motor == 'A':
		GPIO.output(AIN1,GPIO.LOW)
		GPIO.output(AIN2,GPIO.LOW)
	elif motor == 'B':
		GPIO.output(BIN1,GPIO.LOW)
		GPIO.output(BIN2,GPIO.LOW)
	elif motor == 'C':
		GPIO.output(CIN1,GPIO.LOW)
		GPIO.output(CIN2,GPIO.LOW)
	else:
		print('ERROR: No motor called ',str(motor),' !')
def all_stop():
	motor_stop('A')
	motor_stop('B')
	motor_stop('C')
	GPIO.output(STANBY,GPIO.LOW)

try:
	all_stop()
	print(' Use simple commands to test your motor: \n choose motor with letter(A,B,C) \n then direction(C or A/AC) \n or S for stop \n Then add a speed(0-255) \n an example: \n "A-C-200" \n "B-S-0" \n you can exit anytime with ^C \n')

	while True:
		usr_sig = raw_input('Input>')
		motor,direction,speed = usr_sig.split('-')

		speed = int(speed)
		if speed > 255:
			speed = 255
		DC = speed/2.55

		if direction == 'C':
			motor_spin(motor,True,DC)
		elif direction == 'A' or direction == 'AC':
			motor_spin(motor,False,DC)
		elif direction == 'S':
			motor_stop(motor)

except:
	all_stop()
	print(sys.exc_info())
	print('\nGoodBye	\n')
	pwm_out.stop()
	GPIO.cleanup()

