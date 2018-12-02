import sys
sys.path.append('../')
from aoc_utilities.file_utility import readIntoStrArray

boxIds = readIntoStrArray("input.txt")

def findLetterCount(letter, word):
    count = 0
    for wordLetter in word:
        if wordLetter == letter:
            count += 1
    return count

twosCount = 0
threesCount = 0

for boxId in boxIds:
    twoFound = False
    threeFound = False
    for letter in boxId:
        count = findLetterCount(letter, boxId)
        if count == 2 and not twoFound:
            twosCount += 1
            twoFound = True
            continue
        elif count == 3 and not threeFound:
            threesCount += 1
            threeFound = True
            continue
        elif twoFound and threeFound:
            break

print("Checksum = " + str(threesCount * twosCount))