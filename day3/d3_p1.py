import sys
sys.path.append('../')
from aoc_utilities.file_utility import readIntoStrArray

import re
import os

boxIds = readIntoStrArray("input.txt")

class BoundingBox:
        def __init__(self, id, x, y, w, h):
                self.x = x
                self.y = y
                self.w = w + 1
                self.h = h + 1
                self.id = id

class Point:
        def __init__(self, x, y):
                self.x = x
                self.y = y

def getBoxIds(boxIds):
        results = []
        for id in boxIds:
                result = re.findall(r'\d+', id)
                results.append(BoundingBox(int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4])))
        return results

def isPointInBoundingBox(x, y, boundingBox):
        if (boundingBox.x < x and (boundingBox.x + boundingBox.w) > x and boundingBox.y < y and (boundingBox.y + boundingBox.h) > y):
                return True    
        else:
                return False

def areaOverlapPointSweep(bb1, bb2):
        area = 0
        for x in range(bb1.x, bb1.w + bb1.x + 1):
                for y in range(bb1.y, bb1.h + bb1.y + 1):
                        if (isPointInBoundingBox(x, y, bb2)):
                                area += 1
        return area   

def bbOverlap(bb1, bb2):
        topRight = Point(bb1.x + bb1.w, bb1.y)
        bottomLeft = Point(bb1.x, bb1.y + bb1.h)
        bottomRight = Point(bb1.x + bb1.w, bb1.y + bb1.h)
        if (isPointInBoundingBox(bb1.x, bb1.y, bb2) or isPointInBoundingBox(topRight.x, topRight.y, bb2) or isPointInBoundingBox(bottomLeft.x, bottomLeft.y, bb2) or isPointInBoundingBox(bottomRight.x, bottomRight.y, bb2)):
                return True
        else:
                return False

bBs = getBoxIds(boxIds)
           
def findCoord(x, y):
        bbs = []
        for i in range(0, len(bBs)):
                bb = bBs[i]
                if isPointInBoundingBox(x, y, bb):
                        return bb.id
        return None
xmax = 1500
ymax = 1500
overlap = [["." for i in range(ymax)] for i in range(xmax)]

bBsMax = len(bBs)
display = 0
overlapped = False
for i in range(len(bBs)):
        bb = bBs[i]
        os.system("cls")
        display = (i / bBsMax) * 100
        print("CREATING CLAIMS FABRIC")
        print(display, '%')
        overlapped = False
        for y in range(bb.h + bb.y):
                for x in range(bb.w + bb.x):
                        if (isPointInBoundingBox(x, y, bb)):
                                if (overlap[y][x] != "."):
                                        overlapped = True
                                        overlap[y][x] = "X"
                                else:
                                        overlap[y][x] = bb.id
        
print("WRITING FILE")
f = open("test.txt", "w+")
count = 0
for y in range(ymax):
        for x in range(xmax):
                if (overlap[y][x] == "X"):
                        count += 1
                f.write(str(overlap[y][x]))
        f.write("\r\n");
print("COUNT ", count)
f.close()     