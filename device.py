import busio
import board
import numpy as np
from time import sleep
import adafruit_vl53l0x
from time import sleep, time
# from background import reset, init

print("Initializing TOF sensors ...")

i2c = busio.I2C(board.SCL, board.SDA)
def get_distance():
    distance = adafruit_vl53l0x.VL53L0X(i2c)
    sleep(0.1)
    return distance
