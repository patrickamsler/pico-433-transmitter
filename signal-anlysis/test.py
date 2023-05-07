import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    time, amplitude = loaddata()

    #Normalize the amplitude values
    amplitude_norm = np.where(amplitude >= 1.2, 1, 0)
    
    countedges(amplitude_norm)
    
    # display the plot
    plot(time, amplitude_norm)

def plot(time, amplitude):
    # Create a line plot of the data
    plt.plot(time, amplitude)
    # Add axis labels and a title
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Amplitude vs Time')
    plt.show()

def loaddata():
    # Load the data from the CSV file
    data = pd.read_csv('signal-sample/test2/samples-a-on-2.csv', skiprows=[0], header=None, names=['time', 'amplitude'])
    # Extract the time and amplitude values
    time = data['time'].values
    amplitude = data['amplitude'].values
    return time, amplitude

def countedges(amplitude):
    # find the edges
    edges = np.where(np.diff(amplitude) != 0)
    print('Edges: {}'.format(edges))
    
    # Count the number of edges
    numofedges = len(edges[0])
    print('Number of edges: {}'.format(numofedges))
    
    frames = numofedges / 2 / 25 # one edge for positive and one for negative, 25 positive edges per frame
    print('Number of frames: {}'.format(frames))

# Call the main function
main()