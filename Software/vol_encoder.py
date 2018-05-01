#! /usr/bin/env python

#Porting the pigpio rotary_encoder sample to use RPi.GPIO

import RPi.GPIO as GPIO

class decoder:
	def __init__(self, gpioA, gpioB, callback):

		self.lastGpio = None
		self.gpioA = gpioA
		self.gpioB = gpioB
		self.callback = callback

		self.levA = 0
		self.levB = 0

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.gpioA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.gpioB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		GPIO.add_event_detect(self.gpioA, GPIO.BOTH, self._pulse)
		GPIO.add_event_detect(self.gpioB, GPIO.BOTH, self._pulse)

	def _pulse(self, pin):
		level = GPIO.input(pin)
		if pin == self.gpioA:
			self.levA = level
		else:
			self.levB = level

		if pin != self.lastGpio:
			self.lastGpio = pin

			if pin == self.gpioA and level == 1:
				if self.levB == 1:
					self.callback(1)
			elif pin == self.gpioB and level == 1:
				if self.levA == 1:
					self.callback(-1)

	def destroy(self):
		GPIO.remove_event_detect(self.gpioA)
		GPIO.remove_event_detect(self.gpioB)
		GPIO.cleanup()

