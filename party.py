# coding: utf-8
import random
from lib import Factory, FhemHelper

args = Factory.get_arg_parser().parse_args()
logger = Factory.get_logger('Party', args)
for device in args.hue_devices.split(','):
    fhem = FhemHelper(args.fhem_server, [device], logger)
    fhem.rgb(random.randint(0, 0xff), random.randint(0, 0xff), random.randint(0, 0xff))
