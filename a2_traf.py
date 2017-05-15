import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_11",GPIO.OUT)	#R1
GPIO.setup("P8_13",GPIO.OUT)	#Y1
GPIO.setup("P8_15",GPIO.OUT)	#G1

GPIO.setup("P8_12",GPIO.OUT)	#R2
GPIO.setup("P8_14",GPIO.OUT)	#Y2
GPIO.setup("P8_16",GPIO.OUT)	#G2

while True:
	GPIO.output("P8_11",GPIO.HIGH)	#R1 on
	GPIO.output("P8_16",GPIO.HIGH)	#G2 on
	sleep(3)
	GPIO.output("P8_16",GPIO.LOW)	#G2 off
	GPIO.output("P8_14",GPIO.HIGH)	#Y2 on
	sleep(1)
	GPIO.output("P8_11",GPIO.LOW)	#R1 off
	GPIO.output("P8_13",GPIO.HIGH)	#Y1 on
	sleep(1)
	GPIO.output("P8_14",GPIO.LOW)	#Y2 off
	GPIO.output("P8_12",GPIO.HIGH)	#R2 on
	sleep(1)
	GPIO.output("P8_13",GPIO.LOW)	#Y1 off
	GPIO.output("P8_15",GPIO.HIGH)	#G1 on
	sleep(3)
	GPIO.output("P8_15",GPIO.LOW)	#G1 off
	GPIO.output("P8_13",GPIO.HIGH)	#Y1 on
	sleep(1)
	GPIO.output("P8_12",GPIO.LOW)	#R2 off
	GPIO.output("P8_14",GPIO.HIGH)	#Y2 on
	sleep(1)
	GPIO.output("P8_13",GPIO.LOW)	#Y1 off
	GPIO.output("P8_11",GPIO.HIGH)	#R1 on
	sleep(1)
	GPIO.output("P8_14",GPIO.LOW)	#Y2 off
	GPIO.output("P8_16",GPIO.HIGH)	#G2 on
	sleep(3)

