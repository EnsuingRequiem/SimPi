# Notes

The following two commands can view what process is accessing the sound cards  
`fuser -v /dev/snd/*`  
`lsof /dev/snd/*`

`fuser` has an option to kill what is using a specific device. This could be used to kill the audio coming from one source and then swap to another?

`awk -F"[][]" '/dB/ { print $4 }' <(amixer sget Digital)` will find out the current dB level of the music.
