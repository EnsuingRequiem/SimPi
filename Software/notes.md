# Notes

The following two commands can view what process is accessing the sound cards  
`fuser -v /dev/snd/*`  
`lsof /dev/snd/*`

`lsof -F c /dev/snd/pcm* | awk '/^c/ { print substr($1,2) }'` will return just the name of the command using the PCM device for acting upon

`fuser` has an option to kill what is using a specific device. This could be used to kill the audio coming from one source and then swap to another?

`amixer sget Digital | awk -F\"[][]\" '/dB/ {{ print $4 }} NR==6' | awk 'NR > 1 {{ exit }}; 1'` will find out the current dB level of the music.
`amixer sget Digital | awk -F\"[][]\" '/dB/ {{ print $6 }} NR==6' | awk 'NR > 1 {{ exit }}; 1'` will find out the status of sound output.

`sudo systemctl restart librespot` is enough to end the playback from Spotify

Bluetooth was initially wonky (maybe didn't restart after the install of the bluetooth software)

bluetooth process:
 bluetoothctl
 power on
 discoverable on
 pairable on
 agent NoInputNoOutput
 default-agent

 editing the /etc/bluetooth/main.conf timeouts for the purpose of the presentation to not time out

*This will allow running the alsaloop command without hiccups*
 All you need to do is give your "audio" group permissions to access the rtprio, and memlock limits. To do this, you just need to run these commands, which will add some lines to the file /etc/security/limits.conf and add you to the audio user group.:

```
sudo su -c `echo @audio - rtprio 99 >> /etc/security/limits.conf`
sudo su -c `echo @audio - memlock unlimited >> /etc/security/limits.conf`
```

need to find a way to setup a callback for when bluetooth connects or when something starts to use the pcm.
Look more into this page:
https://github.com/Arkq/bluez-alsa/issues/41#issuecomment-286877885
