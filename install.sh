#!/bin/bash

sudo apt-get install -y p7zip-full build-essential minicom htop resolvconf

# Install SIMCom 8200 drivers
wget https://www.waveshare.com/w/upload/f/fb/SIM8200-M2_5G_HAT_code.7z
7z x SIM8200-M2_5G_HAT_code.7z
sudo ./SIM8200-M2_5G_HAT_code/install.sh
sudo grep -q -F 'blacklist qmi_wwan' /etc/modprobe.d/blacklist-modem.conf || sudo echo 'blacklist qmi_wwan' >> sudo /etc/modprobe.d/blacklist-modem.conf
cp ./SIM8200-M2_5G_HAT_code/Goonline/simcom-cm /usr/bin/.
sudo echo "/usr/bin/simcom-cm &" >> /etc/rc.local
rm ./SIM8200-M2_5G_HAT_code.7z
rm -r ./SIM8200-M2_5G_HAT_code

# Install raspap
curl -sL https://install.raspap.com | sudo bash

# create python virtual environment with dependencies
python3 -m virtualenv venv
venv/bin/pip install -e .

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "* * * * * " $PWD/venv/bin/iot-5g-sat>> mycron
#install new cron file
crontab mycron
rm mycron
