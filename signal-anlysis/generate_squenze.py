import json

# Number of edges: 800
# Number of frames: 16.0
# Frame 0: 001101111100001100011100 = 37c31c - frame_length: 0.039000, cycle_length: 0.001513, high_peak: 0.001092, low_peak: 0.000317, preamble_length: 0.002700, preamble_high: 0.000400
# Frame 1: 001101111100001100011100 = 37c31c - frame_length: 0.039000, cycle_length: 0.001513, high_peak: 0.001075, low_peak: 0.000300, preamble_length: 0.002700, preamble_high: 0.000300
# Frame 2: 001101111100001100011100 = 37c31c - frame_length: 0.039100, cycle_length: 0.001517, high_peak: 0.000992, low_peak: 0.000217, preamble_length: 0.002700, preamble_high: 0.000300
# Frame 3: 001101111100001100011100 = 37c31c - frame_length: 0.039000, cycle_length: 0.001517, high_peak: 0.000967, low_peak: 0.000217, preamble_length: 0.002600, preamble_high: 0.000200
# Frame 4: 001101111100001100011100 = 37c31c - frame_length: 0.046600, cycle_length: 0.001521, high_peak: 0.000850, low_peak: 0.000342, preamble_length: 0.010100, preamble_high: 0.002800
# Frame 5: 001101111100001100011100 = 37c31c - frame_length: 0.046600, cycle_length: 0.001521, high_peak: 0.000833, low_peak: 0.000342, preamble_length: 0.010100, preamble_high: 0.002900
# Frame 6: 001101111100001100011100 = 37c31c - frame_length: 0.046600, cycle_length: 0.001517, high_peak: 0.000833, low_peak: 0.000342, preamble_length: 0.010200, preamble_high: 0.002900
# Frame 7: 001101111100001100011100 = 37c31c - frame_length: 0.046700, cycle_length: 0.001521, high_peak: 0.000842, low_peak: 0.000333, preamble_length: 0.010200, preamble_high: 0.002900
# Frame 8: 001110010101000001011100 = 39505c - frame_length: 0.039000, cycle_length: 0.001517, high_peak: 0.000970, low_peak: 0.000229, preamble_length: 0.002600, preamble_high: 0.000200
# Frame 9: 001110010101000001011100 = 39505c - frame_length: 0.039000, cycle_length: 0.001517, high_peak: 0.000980, low_peak: 0.000221, preamble_length: 0.002600, preamble_high: 0.000200
# Frame 10: 001110010101000001011100 = 39505c - frame_length: 0.039000, cycle_length: 0.001517, high_peak: 0.000970, low_peak: 0.000214, preamble_length: 0.002600, preamble_high: 0.000200
# Frame 11: 001110010101000001011100 = 39505c - frame_length: 0.039000, cycle_length: 0.001517, high_peak: 0.000940, low_peak: 0.000186, preamble_length: 0.002600, preamble_high: 0.000200
# Frame 12: 001110010101000001011100 = 39505c - frame_length: 0.046600, cycle_length: 0.001521, high_peak: 0.000820, low_peak: 0.000343, preamble_length: 0.010100, preamble_high: 0.002800
# Frame 13: 001110010101000001011100 = 39505c - frame_length: 0.046600, cycle_length: 0.001521, high_peak: 0.000830, low_peak: 0.000364, preamble_length: 0.010100, preamble_high: 0.002800
# Frame 14: 001110010101000001011100 = 39505c - frame_length: 0.046600, cycle_length: 0.001521, high_peak: 0.000830, low_peak: 0.000357, preamble_length: 0.010100, preamble_high: 0.002800
# Frame 15: 001110010101000001011100 = 39505c - frame_length: 0.103700, cycle_length: 0.003900, high_peak: 0.000830, low_peak: 0.000371, preamble_length: 0.010100, preamble_high: 0.002800

# 3a686c, 37c31c
# Average cycle length: 0.001520
# Average high peak: 0.000921
# Average low peak: 0.000278
# Average preamble length short: 0.002650
# Average preamble length long: 0.010146
# Average preamble high short: 0.000240
# Average preamble high long: 0.002856

# 3a686c, 37c31c
# Average cycle length: 0.001518
# Average high peak: 0.000917
# Average low peak: 0.000277
# Average preamble length short: 0.002631
# Average preamble length long: 0.010171
# Average preamble high short: 0.000238
# Average preamble high long: 0.002868

# 37c31c, 39505c
# Average cycle length: 0.001518
# Average high peak: 0.000922
# Average low peak: 0.000288
# Average preamble length short: 0.002637
# Average preamble length long: 0.010125
# Average preamble high short: 0.000250
# Average preamble high long: 0.002838

# timing in us
cycle_length = 1518
cycle_high_peak = 921
cycle_low_peak = 278
preamble_length_short = 2650
preamble_high_short = 240
preamble_length_long = 10146
preamble_high_long = 2856


def generate():
    # Frame consists of 24 bits and a preamble of 1 bit = 50 edges
    # the sequence is composed of 16 frames = 800 edges

    num_1 = 0x3a686c
    num_2 = 0x37c31c

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
    binary_value = bin(num)[2:]
    for digit in binary_value:
        if digit == '1':
            sequence.append(cycle_high_peak)
            sequence.append(cycle_length - cycle_high_peak)
        else:
            sequence.append(cycle_low_peak)
            sequence.append(cycle_length - cycle_low_peak)

def write_to_file(sequence):
    # Specify the file path for the JSON file
    file_path = "sequence-a-on.json"

    # Write the list to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(sequence, json_file)

generate()
