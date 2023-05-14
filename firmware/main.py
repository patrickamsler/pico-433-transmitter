from transmitter import Transmitter

def on():
    send(True)
    
def off():
    send(False)

def send(on=True, channel='a'):
    # Create a transmitter object
    transmitter = Transmitter()
    transmitter.send(on, channel)