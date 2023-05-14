from transmitter import Transmitter
from pio_test import pio_blink

def send(on=True):
    # Create a transmitter object
    transmitter = Transmitter()
    transmitter.send(on)