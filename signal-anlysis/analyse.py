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
        print('Frame {}: {} = {} - frame_length: {:.6f}, cycle_length: {:.6f}, high_peak: {:.6f}, low_peak: {:.6f}, preamble_length: {:.6f}, preamble_high: {:.6f}'.format(i,
              f['bits'], f['hex'], f['frame_length'], f['cycle_length'], f['high_peak'], f['low_peak'], f['preamble_length'], f['preamble_high']))
        # plot(f['time'], f['amplitude'])

    print_average(frames)
    
def print_average(frames):
    # average cycle length
    cycle_lengths = [f['cycle_length'] for f in frames[:-1]]
    avg_cycle_length = sum(cycle_lengths) / len(cycle_lengths)
    print('Average cycle length: {:.6f}'.format(avg_cycle_length))
    #average high peak
    high_peaks = [f['high_peak'] for f in frames[:-1]]
    avg_high_peak = sum(high_peaks) / len(high_peaks)
    print('Average high peak: {:.6f}'.format(avg_high_peak))
    #average low peak
    low_peaks = [f['low_peak'] for f in frames[:-1]]
    avg_low_peak = sum(low_peaks) / len(low_peaks)
    print('Average low peak: {:.6f}'.format(avg_low_peak))
    #average preamble length
    preamble_lengths_short = [f['preamble_length'] for f in frames if f['preamble_length'] < 0.005]
    avg_preamble_length_short = sum(preamble_lengths_short) / len(preamble_lengths_short)
    print('Average preamble length short: {:.6f}'.format(avg_preamble_length_short))
    preamble_lengths_long = [f['preamble_length'] for f in frames if f['preamble_length'] > 0.005]
    avg_preamble_length_long = sum(preamble_lengths_long) / len(preamble_lengths_long)
    print('Average preamble length long: {:.6f}'.format(avg_preamble_length_long))
    #average preamble high
    preamble_highs_short = [f['preamble_high'] for f in frames if f['preamble_high'] < 0.001]
    avg_preamble_high_short = sum(preamble_highs_short) / len(preamble_highs_short)
    print('Average preamble high short: {:.6f}'.format(avg_preamble_high_short))
    preamble_highs_long = [f['preamble_high'] for f in frames if f['preamble_high'] > 0.001]
    avg_preamble_high_long = sum(preamble_highs_long) / len(preamble_highs_long)
    print('Average preamble high long: {:.6f}'.format(avg_preamble_high_long))

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
    data = pd.read_csv('/Users/patrick/projects/pico-433-transmitter/signal-anlysis/signal-sample/test2/samples-a-on-3.csv',
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
    peak_high = []
    peak_low = []
    
    for i in range(2, len(edges), 2):  # skip first two edges
        if i+2 >= len(edges):
            time_cycle = (time[-1] - time[edges[i]])
            time_peak = (time[edges[i+1]] - time[edges[i]])
        else:
            time_cycle = (time[edges[i+2]] - time[edges[i]])
            time_peak = (time[edges[i+1]] - time[edges[i]])
        cycles.append(time_cycle)
        
        peak_to_cycle = time_peak / time_cycle * 100
        if peak_to_cycle > 50:
            peak_high.append(time_peak) # consider this a high peak
        else:
            peak_low.append(time_peak) # consider this a low peak
        
    avg_cycle_length = sum(cycles) / len(cycles)
    avg_high_peak = sum(peak_high) / len(peak_high)
    avg_low_peak = sum(peak_low) / len(peak_low)
    return avg_cycle_length, avg_high_peak, avg_low_peak


def build_frame(amplitude, time, edges):
    bits = calc_bits(edges, amplitude)
    hex = format(int(bits, 2), 'x')
    cycle_length, high_peak, low_peak = calc_cycle_length(time, edges)
    frame = {
        'time': time,
        'amplitude': amplitude,
        'edges': edges,
        'bits': bits,
        'hex': hex,
        'frame_length': time[-1] - time[0],
        'cycle_length': cycle_length,
        'high_peak': high_peak,
        'low_peak': low_peak,
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
