# coding: utf-8
from lib import Factory

args = Factory.get_arg_parser().parse_args()
logger = Factory.get_logger('Off', args)
fhem = Factory.get_fhem(args, logger)
fhem.rgb(0, 0, 0)
