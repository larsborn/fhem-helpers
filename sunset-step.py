# coding: utf-8
import os
from lib import FhemHelper

MAX_STATE = 10

state_file = os.environ['SUNSET_STATE_FILE']
f = FhemHelper(
    os.environ['FHEM_SERVER'],
    [device.strip() for device in os.environ['HUE_DEVICES'].split(',') if device.strip()]
)

if os.path.exists(state_file):
    with open(state_file, 'r') as fp:
        try:
            current_state = int(fp.read().strip())
        except ValueError:
            current_state = MAX_STATE
else:
    current_state = MAX_STATE

alpha = float(current_state) / MAX_STATE
f.rgb(alpha * 0xfd, alpha * 0x5e, alpha * 0x53)

if current_state == 0:
    os.remove(state_file)
else:
    with open(state_file, 'w') as fp:
        fp.write('%i' % (current_state - 1))
