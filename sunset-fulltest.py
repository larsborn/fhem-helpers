# coding: utf-8
import fhem
import time

f = fhem.Fhem('localhost')
f.connect()

devices = ['HUEDevice1', 'HUEDevice2']


def rgb(r, g, b):
    for device in devices:
        f.send_cmd('set %s rgb %02x%02x%02x' % (device, r, g, b))


for i in range(10, -1, -1):
    alpha = i / 10.0
    rgb(alpha * 0xfd, alpha * 0x5e, alpha * 0x53)
    time.sleep(0.8)
