import fhem
import logging
import os
import argparse
from math import log, exp


class FhemHelper(object):
    def __init__(self, host, devices, logger):
        self.f = fhem.Fhem(host)
        self.f.connect()
        self.devices = devices
        self.logger = logger

    def rgb(self, r, g, b):
        for device in self.devices:
            command = 'set %s rgb %02x%02x%02x' % (device, r, g, b)
            self.logger.debug('Sending command: %s' % command)
            self.f.send_cmd(command)


class ConsoleHandler(logging.Handler):
    def emit(self, record):
        print('[%s] %s' % (record.levelname, record.msg))


class TransitionEffect(object):
    MAX_STATE = 10

    @staticmethod
    def linear(cur):
        return float(cur) / TransitionEffect.MAX_STATE

    @staticmethod
    def exponential(cur):
        a = log(2) / 10
        return exp(a * cur) - 1


class Factory(object):
    @staticmethod
    def get_arg_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--fhem-server',
            default=os.environ['FHEM_SERVER'] if 'FHEM_SERVER' in os.environ else None
        )
        parser.add_argument(
            '--hue-devices',
            default=os.environ['HUE_DEVICES'] if 'HUE_DEVICES' in os.environ else ''
        )
        parser.add_argument('--debug', help='enables debug logging', action='store_true')
        return parser

    @staticmethod
    def get_logger(name, args):
        logger = logging.getLogger(name)
        logger.handlers.append(ConsoleHandler())
        logger.setLevel(logging.DEBUG if args.debug else logging.WARNING)
        return logger

    @staticmethod
    def get_fhem(args, logger):
        return FhemHelper(
            args.fhem_server,
            [device.strip() for device in args.hue_devices.split(',') if device.strip()],
            logger
        )
