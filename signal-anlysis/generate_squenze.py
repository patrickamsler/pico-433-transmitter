import json

# Number of edges: 800
# Number of frames: 16.0
# Frame 0: 001110100110100001101100 = 3a686c - frame_length: 0.039041, cycle_length: 0.001516, high_peak: 0.001090, low_peak: 0.000339, preamble_length: 0.002645, preamble_high: 0.000401
# Frame 1: 001110100110100001101100 = 3a686c - frame_length: 0.039081, cycle_length: 0.001518, high_peak: 0.001028, low_peak: 0.000277, preamble_length: 0.002645, preamble_high: 0.000321
# Frame 2: 001110100110100001101100 = 3a686c - frame_length: 0.039081, cycle_length: 0.001516, high_peak: 0.001006, low_peak: 0.000231, preamble_length: 0.002686, preamble_high: 0.000240
# Frame 3: 001110100110100001101100 = 3a686c - frame_length: 0.039041, cycle_length: 0.001516, high_peak: 0.000991, low_peak: 0.000216, preamble_length: 0.002645, preamble_high: 0.000200
# Frame 4: 001110100110100001101100 = 3a686c - frame_length: 0.046657, cycle_length: 0.001521, high_peak: 0.000849, low_peak: 0.000361, preamble_length: 0.010141, preamble_high: 0.002886
# Frame 5: 001110100110100001101100 = 3a686c - frame_length: 0.046697, cycle_length: 0.001523, high_peak: 0.000864, low_peak: 0.000358, preamble_length: 0.010141, preamble_high: 0.002886
# Frame 6: 001110100110100001101100 = 3a686c - frame_length: 0.046657, cycle_length: 0.001521, high_peak: 0.000842, low_peak: 0.000324, preamble_length: 0.010141, preamble_high: 0.002846
# Frame 7: 001110100110100001101100 = 3a686c - frame_length: 0.046778, cycle_length: 0.001527, high_peak: 0.000842, low_peak: 0.000327, preamble_length: 0.010141, preamble_high: 0.002846
# Frame 8: 001101111100001100011100 = 37c31c - frame_length: 0.039041, cycle_length: 0.001516, high_peak: 0.000952, low_peak: 0.000190, preamble_length: 0.002645, preamble_high: 0.000200
# Frame 9: 001101111100001100011100 = 37c31c - frame_length: 0.039081, cycle_length: 0.001518, high_peak: 0.000949, low_peak: 0.000194, preamble_length: 0.002646, preamble_high: 0.000201
# Frame 10: 001101111100001100011100 = 37c31c - frame_length: 0.039041, cycle_length: 0.001516, high_peak: 0.000959, low_peak: 0.000197, preamble_length: 0.002645, preamble_high: 0.000160
# Frame 11: 001101111100001100011100 = 37c31c - frame_length: 0.039041, cycle_length: 0.001516, high_peak: 0.000952, low_peak: 0.000194, preamble_length: 0.002645, preamble_high: 0.000201
# Frame 12: 001101111100001100011100 = 37c31c - frame_length: 0.046657, cycle_length: 0.001520, high_peak: 0.000808, low_peak: 0.000321, preamble_length: 0.010181, preamble_high: 0.002846
# Frame 13: 001101111100001100011100 = 37c31c - frame_length: 0.046697, cycle_length: 0.001523, high_peak: 0.000855, low_peak: 0.000337, preamble_length: 0.010141, preamble_high: 0.002886
# Frame 14: 001101111100001100011100 = 37c31c - frame_length: 0.046697, cycle_length: 0.001523, high_peak: 0.000828, low_peak: 0.000304, preamble_length: 0.010141, preamble_high: 0.002846
# Frame 15: 001101111100001100011100 = 37c31c - frame_length: 0.093474, cycle_length: 0.003472, high_peak: 0.000802, low_peak: 0.000294, preamble_length: 0.010141, preamble_high: 0.002806
# Average cycle length: 0.001520
# Average high peak: 0.000921
# Average low peak: 0.000278
# Average preamble length short: 0.002650
# Average preamble length long: 0.010146
# Average preamble high short: 0.000240
# Average preamble high long: 0.002856

# a-on-1
# 3a686c, 37c31c
# Average cycle length: 0.001520
# Average high peak: 0.000921
# Average low peak: 0.000278
# Average preamble length short: 0.002650
# Average preamble length long: 0.010146
# Average preamble high short: 0.000240
# Average preamble high long: 0.002856

# a-on-2
# 3a686c, 37c31c
# Average cycle length: 0.001518
# Average high peak: 0.000917
# Average low peak: 0.000277
# Average preamble length short: 0.002631
# Average preamble length long: 0.010171
# Average preamble high short: 0.000238
# Average preamble high long: 0.002868

# a-on-3
# 37c31c, 39505c
# Average cycle length: 0.001518
# Average high peak: 0.000922
# Average low peak: 0.000288
# Average preamble length short: 0.002637
# Average preamble length long: 0.010125
# Average preamble high short: 0.000250
# Average preamble high long: 0.002838

# timing in us
cycle_length = 1520
cycle_high_peak = 921
cycle_low_peak = 278
preamble_length_short = 2650
preamble_high_short = 240
preamble_length_long = 10146
preamble_high_long = 2856


def generate():
    # Frame consists of 24 bits and a preamble of 1 bit = 50 edges
    # the sequence is composed of 16 frames = 800 edges

    num_1 = 0x35acbc
    num_2 = 0x33397c

    sequence = [0]
    for f in range(16):  # 16 frames
        if f < 8:  # first 8 frames, num_1
            if f < 4:
                short_preamble(sequence)
            else:
                long_preamble(sequence)
            sequence_24_bits(sequence, num_1)
        else:  # last 8 frames, num_2
            if f < 12:
                short_preamble(sequence)
            else:
                long_preamble(sequence)
            sequence_24_bits(sequence, num_2)

    print(sequence)
    write_to_file(sequence)

def short_preamble(sequence):
    sequence.append(preamble_high_short)
    sequence.append(preamble_length_short - preamble_high_short)


def long_preamble(sequence):
    sequence.append(preamble_high_long)
    sequence.append(preamble_length_long - preamble_high_long)


def sequence_24_bits(sequence, num):
    binary_value = bin(num)[2:].zfill(24)
    print(binary_value)
    for digit in binary_value:
        if digit == '1':
            sequence.append(cycle_high_peak)
            sequence.append(cycle_length - cycle_high_peak)
        else:
            sequence.append(cycle_low_peak)
            sequence.append(cycle_length - cycle_low_peak)


def write_to_file(sequence):
    # Specify the file path for the JSON file
    file_path = "sequence-a-off.json"

    # Write the list to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(sequence, json_file)

generate()
