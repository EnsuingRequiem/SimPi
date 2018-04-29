#! /usr/bin/env python

from time import sleep
import pigpio
import rotary_encoder

pos = 0

def callback(way):
	global pos
	pos += way
	print("pos={}".format(pos))

pi = pigpio.pi()
decoder = rotary_encoder.decoder(pi, 13, 26, callback)
time.sleep(300)
decoder.cancel()
pi.stop()
