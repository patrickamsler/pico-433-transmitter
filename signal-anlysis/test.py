import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():
    time, amplitude = loaddata()

    # Normalize the amplitude values
    amplitude_norm = np.where(amplitude >= 1.2, 1, 0)
    # plot full signal
    # plot(time, amplitude_norm)

    edges = find_edges(amplitude_norm)

    frames = find_frames(amplitude_norm, time, edges)
    for i, f in enumerate(frames):
        print('Frame {}: {} = {} - frame_length: {}, period: {:.10f}, preamble_length: {}, preamble_high: {}'.format(i,
              f['bits'], f['hex'], f['frame_length'], f['cycle_length'], f['preamble_length'], f['preamble_high']))
        plot(f['time'], f['amplitude'])


def plot(time, amplitude):
    # Create a line plot of the data
    plt.plot(time, amplitude)
    # Add axis labels and a title
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Amplitude vs Time')
    num_ticks = 20
    x_ticks = np.linspace(time[0], time[-1], num_ticks)
    plt.xticks(x_ticks)
    plt.show()


def loaddata():
    # Load the data from the CSV file
    data = pd.read_csv('/Users/patrick/projects/pico-433-transmitter/signal-anlysis/signal-sample/test2/samples-a-on-1.csv',
                       skiprows=[0], header=None, names=['time', 'amplitude'])
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


def calc_bits(edges, amplitude):
    bits = ''
    for i in range(2, len(edges), 2):
        first_edge = edges[i]
        if i+2 >= len(edges):
            second_edge = len(amplitude)
        else:
            second_edge = edges[i+2]
        amp_sub = amplitude[first_edge:second_edge]
        # check if array contains more zeros or ones
        if np.count_nonzero(amp_sub) > len(amp_sub)/2:
            bits += '1'
        else:
            bits += '0'
    return bits


def calc_cycle_length(time, edges):
    cycles = []
    for i in range(2, len(edges), 2):  # skip first two edges
        if i+2 >= len(edges):
            time_cycle = (time[-1] - time[edges[i]])
        else:
            time_cycle = (time[edges[i+2]] - time[edges[i]])
        cycles.append(time_cycle)
    avg_cycle_length = sum(cycles) / len(cycles)
    return avg_cycle_length


def build_frame(amplitude, time, edges):
    bits = calc_bits(edges, amplitude)
    hex = format(int(bits, 2), 'x')
    frame = {
        'time': time,
        'amplitude': amplitude,
        'edges': edges,
        'bits': bits,
        'hex': hex,
        'frame_length': time[-1] - time[0],
        'cycle_length': calc_cycle_length(time, edges),
        'preamble_length': time[edges[2]] - time[0],
        'preamble_high': time[edges[1]] - time[0],
    }
    return frame


def find_frames(amplitude, time, edges):
    # one edge for positive and one for negative, 25 positive edges per frame
    num_of_frames = len(edges) / 2 / 25
    print('Number of frames: {}'.format(num_of_frames))
    # split the amplitude into frames
    edges_arr = np.split(edges, num_of_frames)
    frames = []
    for i, e in enumerate(edges_arr):
        first = e[0]
        if i+1 >= len(edges_arr):
            last = len(amplitude)
        else:
            last = edges_arr[i+1][0]

        amp_sub = amplitude[first:last]
        time_sub = time[first:last] - time[first]
        e_norm = e - e[0]

        frames.append(build_frame(amp_sub, time_sub, e_norm))
    return frames


# Call the main function
main()
