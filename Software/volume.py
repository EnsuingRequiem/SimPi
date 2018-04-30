#! /usr/bin/env python

import time
import pigpio
import subprocess
import rotary_encoder
import shlex

awk_cmd = 'amixer sget Digital | awk -F"[][]" \'/dB/ { print $4 } NR==6\' | awk \'NR > 1 { exit }; 1\''
args = shlex.split(awk_cmd)
vol = subprocess.Popen(args)
print vol

def rot_callback(way):
    global vol
    pos += way
    print ("vol={}".format(vol))

pi = pigpio.pi()

decoder = rotary_encoder.decoder(pi, 13, 26, rot_callback)

time.sleep(300)

decoder.cancel()

pi.stop()
