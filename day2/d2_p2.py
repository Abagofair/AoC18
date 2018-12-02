import sys
sys.path.append('../')
from aoc_utilities.file_utility import readIntoStrArray

boxIds = readIntoStrArray("input.txt")

def method(boxIds):
    length = len(boxIds[0])
    for i in range(0, len(boxIds), 1):
        firstBoxId = boxIds[i]
        for j in range(i+1, len(boxIds), 1):
            secondBoxId = boxIds[j]
            i = 0
            difference = 0
            index = 0
            while i < length:
                if firstBoxId[i] != secondBoxId[i]:
                    difference += 1
                    index = i
                i += 1
            if difference == 1:
                return [firstBoxId, secondBoxId, index]

solution = method(boxIds)
print(solution[0][:solution[2]] + solution[0][(solution[2]+1):])