#! /usr/bin/env python

#Porting the pigpio rotary_encoder sample to use RPi.GPIO
import RPi.GPIO as GPIO

class decoder:
    def __init__(self, gpioA, gpioB, callback, btn_pin=None, btn_callback=None, tgl_btnpin=None, tgl_callback=None):

        self.lastGpio = None
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.callback = callback

        self.btn_pin = btn_pin
        self.btn_callback = btn_callback
        self.tgl_btnpin = tgl_btnpin
        self.tgl_callback = tgl_callback

        self.levA = 0
        self.levB = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpioA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.gpioB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self.gpioA, GPIO.BOTH, self._pulse)
        GPIO.add_event_detect(self.gpioB, GPIO.BOTH, self._pulse)

        if self.btn_pin:
            GPIO.setup(self.btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(self.btn_pin, GPIO.FALLING, self._press, bouncetime=500)

        if self.tgl_btnpin:
            GPIO.setup(self.tgl_btnpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(self.tgl_btnpin, GPIO.FALLING, self._toggle, bouncetime=500)

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
        if self.btn_pin:
            GPIO.remove_event_detect(self.btn_pin)
        if self.tgl_btnpin:
            GPIO.remove_event_detect(self.tgl_btnpin)
        GPIO.cleanup()

    def _press(self, pin):
        self.btn_callback(GPIO.input(pin))

    def _toggle(self, tglpin):
        self.tgl_callback(GPIO.input(tglpin))
