import sys
sys.path.append('../')

from aoc_utilities.file_utility import readIntoStrArray

freqChanges = readIntoStrArray("input.txt")

frequency = 0
for freq in freqChanges:
    change = freq[0]
    if change == "-":
        frequency -= int(freq[1:])
    elif change == "+":
        frequency += int(freq[1:])
print(frequency)