from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='iot_5g_sat',
    packages=['iot_5g_sat'],
    python_requires='>=3.7, <4',
    install_requires=required,
    entry_points={
        'console_scripts': ['iot-5g-sat=iot_5g_sat:main'],
    }
)