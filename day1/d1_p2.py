import sys
sys.path.append('../')

from aoc_utilities.file_utility import readIntoStrArray

freqChanges = readIntoStrArray("input.txt")

frequency = 0
frequencies = {}
found = False
while not found:
    for freq in freqChanges:
        change = freq[0]
        changeValue = int(freq[1:])
        if change == "-":
            frequency -= changeValue
        elif change == "+":
            frequency += changeValue

        if frequencies.get(frequency) == frequency:
            print(frequency)
            found = True
            break
        else:
            frequencies[frequency] = frequency