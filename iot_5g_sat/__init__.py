import requests
import json
import serial
import time
import board
import logging

from adafruit_bmp280 import Adafruit_BMP280_I2C
from adafruit_rockblock import RockBlock
from iot_5g_sat.config import get_proxy_url, proxy_token, rb_serial_interface, LOG_LEVEL, LOG_FORMAT

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def build_message(bmp280):
    msg = dict(
        token=proxy_token,
        temperature=bmp280.temperature,
        pressure=bmp280.pressure,
        altitude=bmp280.altitude
    )

    return msg, {
        "imei": "5Gmodem",
        "serial": 0,
        "momsn": 0,
        "transmit_time": "",
        "iridium_latitude": 51.85,
        "iridium_longitude": -0.96142,
        "iridium_cep": 0,
        "data": f"{msg}".encode().hex()
    }


def sbd_transfer(rb:RockBlock):
    # try a satellite Short Burst Data transfer
    status = rb.satellite_transfer()
    # loop as needed
    retry = 0
    while status[0] > 8:
        time.sleep(5)
        status = rb.satellite_transfer()
        retry += 1


def main():

    # Create sensor object, communicating over the board's default I2C bus
    i2c = board.I2C()  # uses board.SCL and board.SDA
    bmp280 = Adafruit_BMP280_I2C(i2c, address=0x76)

    # change this to match the location's pressure (hPa) at sea level
    bmp280.sea_level_pressure = 1013.25

    logger.info("Temperature: %0.1f C" % bmp280.temperature)
    logger.info("Pressure: %0.1f hPa" % bmp280.pressure)
    logger.info("Altitude = %0.2f meters" % bmp280.altitude)

    msg, data = build_message(bmp280)

    try:
        logger.info("Sending through 5G Modem...")
        r = requests.post(get_proxy_url(), data=json.dumps(data), timeout=10)
        r.raise_for_status()
    except Exception as e:
        # If message can't be sent through default OS interface, try satellite
        logger.info("Couldn't be sent through 5G Modem.")
        with serial.Serial(rb_serial_interface, baudrate=19200) as serial_conn:
            rb = RockBlock(serial_conn)
            rb.text_out = json.dumps(msg)
            logger.info("Sending through Satellite...")
            sbd_transfer(rb)
            logger.info("DONE.")
