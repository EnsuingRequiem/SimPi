#! /usr/bin/env python
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPI.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your scrpit")
from time import sleep

counter = 10
Enc_A = 13
Enc_B = 26

def init():
	GPIO.setwarnings(True)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Enc_A, GPIO.IN)
	GPIO.setup(Enc_B, GPIO.IN)
	GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=2)
	return

def rotation_decode(Enc_A):
	global counter
	Switch_A = GPIO.input(Enc_A)
	Switch_B = GPIO.input(Enc_B)

	if (Switch_A == 1) and (Switch_B == 0) :
		counter += 1
		print "direction -> ", counter
		while Switch_B == 0:
			Switch_B = GPIO.input(Enc_B)
		while Switch_B == 1:
			Switch_B = GPIO.input(Enc_B)
		return

	elif (Switch_A == 1) and (Switch_B == 1) :
		counter -= 1
		print "direction -> ", counter
		while Switch_A == 1:
			Switch_A = GPIO.input(Enc_A)
		return

	else:
		return

def main():

	try:
		init()
		while True :
			sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()

if __name__ == '__main__':
	main()
