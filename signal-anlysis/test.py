import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    time, amplitude = loaddata()

    #Normalize the amplitude values
    amplitude_norm = np.where(amplitude >= 1.2, 1, 0)
    # plot full signal
    #plot(time, amplitude_norm)

    edges = find_edges(amplitude_norm)

    frames = find_frames(amplitude_norm, time, edges)
    for f in frames:
        plot(f['time'], f['amplitude'])
    
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
    data = pd.read_csv('signal-sample/test2/samples-a-on-1.csv', skiprows=[0], header=None, names=['time', 'amplitude'])
    # Extract the time and amplitude values
    time = data['time'].values
    amplitude = data['amplitude'].values
    return time, amplitude

def find_edges(amplitude):
    # find the edges
    edges = np.where(np.diff(amplitude) != 0)
    # Count the number of edges
    num_of_edges = len(edges[0])
    print('Number of edges: {}'.format(num_of_edges))
    return edges[0]

def find_frames(amplitude, time, edges):
    # one edge for positive and one for negative, 25 positive edges per frame
    num_of_frames = len(edges) / 2 / 25
    print('Number of frames: {}'.format(num_of_frames))
    # split the amplitude into frames
    edges_arr = np.split(edges, num_of_frames)
    frames = []
    for e in edges_arr:
        amp_sub = amplitude[e[0]:e[-1]+2]
        time_sub = time[e[0]:e[-1]+2]
        frames.append({'time': time_sub, 'amplitude': amp_sub})
    return frames

# Call the main function
main()