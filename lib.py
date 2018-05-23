import fhem

class FhemHelper(object):
    def __init__(self, host, devices):
        self.f = fhem.Fhem(host)
        self.f.connect()
        self.devices = devices

    def rgb(self, r, g, b):
        for device in self.devices:
            self.f.send_cmd('set %s rgb %02x%02x%02x' % (device, r, g, b))

