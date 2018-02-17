import RPi.GPIO as GPIO
from time import sleep
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

IN1 = 13
IN2 = 19
ENA = 16
IN3 = 7
IN4 = 8
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

duty_cycle_direction = 90

direction_PWM = GPIO.PWM(ENA, 100)
direction_PWM.start(duty_cycle_direction)


def motor(way):
	if way == -1:
			GPIO.output(IN1, GPIO.HIGH)
			GPIO.output(IN2, GPIO.LOW)
	elif way == 0:
			GPIO.output(IN1, GPIO.LOW)
			GPIO.output(IN2, GPIO.LOW)
	elif way == 1:
			GPIO.output(IN1, GPIO.LOW)
			GPIO.output(IN2, GPIO.HIGH)

def steering(way):
	if way == -1:
			GPIO.output(IN3, GPIO.HIGH)
			GPIO.output(IN4, GPIO.LOW)
	elif way == 0:
			GPIO.output(IN3, GPIO.LOW)
			GPIO.output(IN4, GPIO.LOW)
	elif way == 1:
			GPIO.output(IN3, GPIO.LOW)
			GPIO.output(IN4, GPIO.HIGH)

light = "off"
leftlight = 2
rightlight = 3
GPIO.setup(leftlight,GPIO.OUT)
GPIO.setup(rightlight,GPIO.OUT)


def lights(switch):
	global light
	light = switch
	if light == "on":
		GPIO.output(leftlight, GPIO.HIGH)
		GPIO.output(rightlight, GPIO.HIGH)
	elif light == "off":
		GPIO.output(leftlight, GPIO.LOW)
		GPIO.output(rightlight, GPIO.LOW)







