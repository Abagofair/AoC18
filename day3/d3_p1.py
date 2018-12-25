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

def aabbCollision(aabb1, aabb2):
        if (aabb1.x < (aabb2.x + aabb2.w) and (aabb1.x + aabb1.w) > aabb2.x and aabb1.y < (aabb2.y + aabb2.h) and (aabb1.h + aabb1.y) > aabb2.y):
                return True
        return False

bBs = getBoxIds(boxIds)
bBcopy = []
for i in range(len(bBs)):
        bBcopy.append(bBs[i].id)
#p2
""" for i in range(len(bBs)):
        overlap = False
        aabb1 = bBs[i]
        for j in range(i+1, len(bBs)):
                aabb2 = bBs[j]
                if (aabbCollision(aabb1, aabb2)):
                        overlap = True
                        try:
                                bBcopy.remove(aabb2.id)
                        except:
                                print('error')
        if overlap:
                try:
                        bBcopy.remove(aabb1.id)
                except:
                        print('error')
print(bBcopy) """

#p1
""" xmax = 1500
ymax = 1500
overlap = [["." for i in range(ymax)] for i in range(xmax)] """

""" bBsMax = len(bBs)
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
f.close() """     