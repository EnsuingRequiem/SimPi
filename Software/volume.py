#! /usr/bin/env python

import time
import pigpio
import subprocess
import rotary_encoder
import shlex

awk_cmd = 'awk -F"[][]" '/dB/ { print $4 } NR==6' <(amixer sget Digital) | awk 'NR > 1 { exit }; 1''
args = shlex.split(awk_cmd)
vol = subprocess.Popen(args)
print vol

def rot_callback(way):
    global vol
    pos += way
    print ("pos={}".format(pos))

pi = pigpio.pi()

decoder = rotary_encoder.decoder(pi, 13, 26, rot_callback)

time.sleep(300)

decoder.cancel()

pi.stop()
