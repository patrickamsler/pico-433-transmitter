import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.arange(0, 1.1, 0.1)
y = np.sin(2*np.pi*x)

# Create a line plot of the data
plt.plot(x, y)

# Get the x-tick locations and calculate the tick interval
tick_locs = plt.xticks()[0]
tick_interval = tick_locs[1] - tick_locs[0]

# Print the tick interval
print('X-axis tick interval:', tick_interval)

# Show the plot
plt.show()