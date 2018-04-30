#! /usr/bin/env python

import time
import pigpio
import subprocess
import rotary_encoder
import shlex
from subprocess import PIPE as PIPE

awk_cmd = subprocess.Popen(["amixer sget Digital | awk -F\"[][]\" '/dB/ {{ print $4 }} NR==6' | awk 'NR > 1 {{ exit }}; 1'"], stdout=PIPE, shell=True)

#amix_cmd = subprocess.Popen(["amixer", "sget", "Digital"], stdout=PIPE)
#awk_cmd1 = subprocess.Popen(["awk", "-F\"[][]\" '/dB/ { print $4 } NR==6'"], stdin=amix_cmd.stdout, stdout=PIPE)
#awk_cmd2 = subprocess.Popen(["awk", "'NR > 1 { exit }; 1'"], stdin=awk_cmd1.stdout, stdout=PIPE)
#amix_args = shlex.split(amix_cmd)
#awk1_args = shlex.split(awk_cmd1)
#awk2_args = shlex.split(awk_cmd2)
#print (amix_args)
#print (awk1_args)
#print (awk2_args)
#amix_cmd.stdout.close()
#awk_cmd1.stdout.close()
vol = awk_cmd.communicate()[0]
#vol = subprocess.Popen(args)
print vol

def rot_callback(way):
    global vol
    if way > 0:
        adj = "%sdB+" % (way)
        subprocess.Popen(["amixer", "sset", "Digital", adj])
    if way < 0:
        adj = "%sdB-" % (way)
        subprocess.Popen(["amixer", "sset", "Digital", adj])
    awk_cmd = subprocess.Popen(["amixer sget Digital | awk -F\"[][]\" '/dB/ {{ print $4 }} NR==6' | awk 'NR > 1 {{ exit }}; 1'"], stdout=PIPE, shell=True)
    vol = awk_cmd.communicate()[0]
    print ("vol={}".format(vol))

pi = pigpio.pi()

decoder = rotary_encoder.decoder(pi, 13, 26, rot_callback)

time.sleep(300)

decoder.cancel()

pi.stop()
