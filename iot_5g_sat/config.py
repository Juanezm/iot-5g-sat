import os
from logging import INFO

LOG_FORMAT = '%(asctime)s - %(levelname)6s - %(message)s'
LOG_LEVEL = INFO

proxy_token = os.environ.get('PROXY_TOKEN', 'my-token')
rb_serial_interface = os.environ.get('RB_SERIAL_IFACE', '/dev/ttyUSB0')

def get_proxy_url() -> str:
    proxy_host = os.environ.get('PROXY_HOST', 'localhost')
    proxy_port = os.environ.get('PROXY_PORT', 8080)
    return f"http://{proxy_host}:{proxy_port}"
