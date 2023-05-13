import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json


def plot():
    time, amplitude_norm = read_signal_norm('signal-sample/test2/samples-a-on-1.csv')
    time_gen, amplitude_gen = read_sequence_norm('sequence-a-on.json')
    
    # Create a line plot of the original data
    plt.plot(time, amplitude_norm, label='Signal org.')
    
    # Create a line plot of the generated data
    plt.plot(time_gen, amplitude_gen, label='Signal gen')

    # Add axis labels and a title
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Amplitude vs Time')
    plt.legend()

    # Display the plot
    plt.show()


def read_signal_norm(file_path):
    # Load the data from the CSV file
    data = pd.read_csv(file_path, skiprows=[0], header=None, names=['time', 'amplitude'])

    # Extract the time and amplitude values
    time = data['time'].values
    amplitude = data['amplitude'].values

    # Normalize the amplitude values
    amplitude_norm = np.where(amplitude >= 1.2, 1, 0)

    # find first edge
    first_edge = np.where(np.diff(amplitude_norm) != 0)[0][0]

    # remove everything before first edge
    time = time[first_edge:]
    amplitude_norm = amplitude_norm[first_edge:]
    # remove offset from time
    time = time - time[0]

    return time, amplitude_norm


def read_sequence_norm(file_path):
    sequence_ms = read_sequence_from_file(file_path)
    # sequence from microsecond to second
    sequence_sec = [x/1000000 for x in sequence_ms]
    time = [0]
    amplitude = [1]
    for i in range(1, len(sequence_sec)):
        time.append(time[-1] + sequence_sec[i])
        if i % 2 == 0:
            amplitude.append(1)
        else:
            amplitude.append(0)
    return time, amplitude


def read_sequence_from_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data


plot()
