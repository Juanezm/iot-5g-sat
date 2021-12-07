#!/bin/bash

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
