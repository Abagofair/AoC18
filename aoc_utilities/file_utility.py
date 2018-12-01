def readIntoStrArray(fileName):
    file = open(fileName, "r")
    strArray = []
    fileStr = file.readline()
    while fileStr != "":
        fileStr = fileStr.split("\n")[0]
        strArray.append(fileStr)
        fileStr = file.readline()
    return strArray