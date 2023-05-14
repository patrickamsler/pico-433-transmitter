from machine import Pin
import ujson
import utime


class Transmitter:
    def __init__(self):
        self.out = Pin(26, Pin.OUT)
        self.data = self.load_data()

    def load_data(self):
        with open('data.json', 'r') as file:
            content = file.read()
            return ujson.loads(content)

    def send(self, on=True, channel='a'):
        self.out.value(0) # set the output low
        for t in self.data[channel]['on' if on else 'off']:
            self._wait_us(t)
            # toggle the output
            self.out.value(0 if self.out.value() else 1)
        self.out.value(0) # set the output low at the end
        
    def _wait_us(self, us):
        ticks = utime.ticks_us()
        while utime.ticks_diff(utime.ticks_us(), ticks) < us:
            pass