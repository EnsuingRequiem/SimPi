#! /usr/bin/env python

import time
#import pigpio
import subprocess
import vol_encoder
#import shlex
import RPi.GPIO as GPIO
from subprocess import PIPE as PIPE

def rot_callback(way):
    global vol
    #print way
    if way > 0:
        adj = "%sdB+" % (way)
        #print adj
        subprocess.Popen(["amixer", "-q", "sset", "Digital", adj])
    if way < 0:
        adj = "%sdB-" % (abs(way))
        #print adj
        subprocess.Popen(["amixer", "-q", "sset", "Digital", adj])
    #awk_cmd = subprocess.Popen(["amixer sget Digital | awk -F\"[][]\" '/dB/ {{ print $4 }} NR==6' | awk 'NR > 1 {{ exit }}; 1'"], stdout=PIPE, shell=True)
    #vol = awk_cmd.communicate()[0]
    #print ("vol={}".format(vol))

def btn_callback(level):
    subprocess.Popen(["amixer", "-q", "sset", "Digital", "toggle"])
try:
    decoder = vol_encoder.decoder(13, 26, rot_callback, 23, btn_callback)
    time.sleep(3000)
except KeyboardInterrupt:
    print "\nVolume Control Cancelled"

#except:
#    print "Some error or exception ocurred."
#
finally:
    decoder.destroy()
    #decoder.cancel()
    #pi.stop()

    #amixer sget Digital | awk -F\"[][]\" '/dB/ {{ print $6 }} NR==6' | awk 'NR > 1 {{ exit }}; 1'
    #above command can be passed to get the current 'sound status' (on|off = unmuted|muted)
    #the amixer command to toggle each setting: (on|off = mute|unmute)
    #
    #awk_cmd = subprocess.Popen(["amixer sget Digital | awk -F\"[][]\" '/dB/ {{ print $4 }} NR==6' | awk 'NR > 1 {{ exit }}; 1'"], stdout=PIPE, shell=True)
    #vol = awk_cmd.communicate()[0]
