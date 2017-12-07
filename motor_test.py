import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

IN2 = 3
IN1 = 5
PWM = 12
STANBY = 16



GPIO.setup(IN2,GPIO.OUT)		#B-IN2
GPIO.setup(IN1,GPIO.OUT)		#B-IN1
GPIO.setup(PWM,GPIO.OUT)		#B-PWM
pwm_out = GPIO.PWM(PWM,100)		#pwm class setup as pwm_out
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
	print('Motor is OFF \n')
	sleep(0.5)
	print(' Use simple commands to test your motor: \n C = clockwise \n A or AC = anit-colckwise \n S = stop \n Then add a speed(0-255) \n and finally a delay time(seconds) \n an example: \n "C 200 3" \n you can exit anytime with ^C \n')

	while True:
		usr_sig = input('Input>')
		direction,speed,delay = usr_sig.split(' ')
		if speed > 255:
			speed = 255
		DC = speed/2.55
		if direction == 'C':
			motor_spin(True,DC)
		elif direction == 'A' or direction == 'AC':
			motor_spin(False,DC)
		elif direction == 'S':
			motor_stop()
		sleep(delay)

except KeyboardInterrupt:
	print('\nGoodBye	\n')
	pwm_out.stop()
	GPIO.cleanup()

