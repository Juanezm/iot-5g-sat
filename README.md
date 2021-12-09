# IoT 5G-Sat

This python module is meant to be used as a cron job in a Raspberry Pi to perform a sensor (BMP280) reading and send
this one to a remote proxy for their corresponding storage.

It uses a RockBlock board for sending the data using an Iridium SBD 9602 in the case that the default 5G interface isn't
available.

## Deployment

A RaspiOS image with `5.4.51` kernel version must be used for this deployment and can be downloaded from:

https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2020-08-24/2020-08-20-raspios-buster-armhf.zip

Copy/clone the content of this repo to the RPi and run the install script

```bash
pi@raspberrypi:~/iot-5G-Sat $ ./install.sh
```

If everything goes well, a new entry will appear in the crontab list

```bash
pi@raspberrypi:~/iot-5G-Sat $ crontab -l
* * * * *  /home/pi/iot-5G-Sat/venv/bin/iot-5g-sat
```

Also, for testing the module can be run at any moment

```bash
pi@raspberrypi:~/iot-5G-Sat $ $PWD/venv/bin/iot-5g-sat
2021-12-07 16:15:12,884 -   INFO - Temperature: 26.6 C
2021-12-07 16:15:12,925 -   INFO - Pressure: 980.6 hPa
2021-12-07 16:15:12,966 -   INFO - Altitude = 275.45 meters
```

## Configuration

This module can be configured using environment variables.

- **PROXY_HOST** IP where the proxy is deployed on.
- **PROXY_PORT** Port used by the proxy.
- **PROXY_TOKEN** Token used in the Proxy for storing the data.
- **RB_SERIAL_IFACE** Serial interface where RockBlock is connected to.

To modify their values:

```bash
export PROXY_HOST=localhost
export PROXY_PORT=8080
export PROXY_TOKEN=my-token
export RB_SERIAL_IFACE=/dev/ttyUSB0
```