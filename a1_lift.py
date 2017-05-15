import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_12",GPIO.IN)	#Switch floor 1
GPIO.setup("P8_14",GPIO.IN)	#Switch floor 3
GPIO.setup("P8_16",GPIO.IN)	#Switch floor 3

GPIO.setup("P8_11",GPIO.OUT)	#LED floor 1
GPIO.setup("P8_13",GPIO.OUT)	#LED floor 2
GPIO.setup("P8_15",GPIO.OUT)	#LED floor 3

last=1
s="Lift is at Floor: "
o="Opening Door at Floor: "
c="Closing Door at Floor: "
while True: 
	if GPIO.input("P8_12")==1:
		GPIO.output("P8_11",GPIO.HIGH)
		if last==1 :
			print s+"1"
			sleep(1)
			print o+"1"
			sleep(1)
			print c+"1"
			
		elif last==2:
			GPIO.output("P8_13",GPIO.LOW)
			
			print s+"2"
			sleep(1)
			print s+"1"
			sleep(1)
			print o+"1"
			sleep(1)
			print c+"1"

		elif last==3:
			GPIO.output("P8_15",GPIO.LOW)
			
			print s+"3"
			sleep(1)
			print s+"2"
			sleep(1)
			print s+"1"
			sleep(1)
			print o+"1"
			sleep(1)
			print c+"1"
				
		last=1
		
	elif GPIO.input("P8_14")==1:
		GPIO.output("P8_13",GPIO.HIGH)
		if last==1 :
			GPIO.output("P8_11",GPIO.LOW)
			
			print s+"1"
			sleep(1)
			print s+"2"
			sleep(1)
			print o+"2"
			sleep(1)
			print c+"2"

		elif last==2:
			print s+"2"
			sleep(1)
			print o+"2"
			sleep(1)
			print c+"2"

		elif last==3:
			GPIO.output("P8_15",GPIO.LOW)
			print s+"3"
			sleep(1)
			print s+"2"
			sleep(1)
			print o+"2"
			sleep(1)
			print c+"2"	
		last=2
		
	elif GPIO.input("P8_16")==1:
		GPIO.output("P8_15",GPIO.HIGH)
		if last==1 :
			GPIO.output("P8_11",GPIO.LOW)

			print s+"1"
			sleep(1)
			print s+"2"
			sleep(1)
			print s+"3"
			sleep(1)
			print o+"3"
			sleep(1)
			print c+"3"

		elif last==2:
			GPIO.output("P8_13",GPIO.LOW)

			print s+"2"
			sleep(1)
			print s+"3"
			sleep(1)
			print o+"3"
			sleep(1)
			print c+"3"

		elif last==3:

			print s+"3"
			sleep(1)
			print o+"3"
			sleep(1)
			print c+"3"	
		last=3


