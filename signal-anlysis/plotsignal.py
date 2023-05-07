import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data from the CSV file
data = pd.read_csv('signal-sample/test1/a-button-on.csv', skiprows=[0], header=None, names=['time', 'amplitude'])

# Extract the time and amplitude values
time = data['time'].values
amplitude = data['amplitude'].values

# Normalize the amplitude values
amplitude_norm = np.where(amplitude >= 1.2, 1, 0)

# Create a line plot of the data
plt.plot(time, amplitude_norm)

# Add axis labels and a title
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Amplitude vs Time')

# Display the plot
plt.show()