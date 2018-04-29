# Software Process

Based on the Max2Play image

Software modifications
```
sudo apt-get update
sudo apt-get install -y python-dev python3-rpi.gpio
sudo apt-get purge wiringpi
hash -r
sudo apt-get install -y git-core
git clone git://git.drogon.net/wiringPi
cd ~/wiringPi
git pull origin
./build
cd ~
sudo apt-get install -y python-pip python3-pip
pip install pyalsaadio
```
