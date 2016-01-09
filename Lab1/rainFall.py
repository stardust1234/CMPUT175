#-------------------------------------------------------------------------------
# Name:        Lab1_rainFall
# Purpose:
#
# Author:      Zhao
#
# Created:     08/01/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def toFloat(rainfall):
    floatRainfall = rainfall.replace('\n','')
    return float(floatRainfall)

def getShortedNo(a):
    return a[:a.find('.')+2]

def readFile(fileName):
    file = []
    for i in fileName.readlines():
        locations = i.split()[0]
        rainFalls = toFloat(getShortedNo(i.split()[1]))
        file.append([locations,rainFalls])
    return file

def writeFile(fileName, sortedFile):
    fileWrite = open(fileName, 'w')
    writed = [False] * 4
    for i in sortedFile:
        i[0] = i[0].rjust(25)
        if i[1] < 70 and writed[0] == False:
           fileWrite.write('\nCities that rainfall is between 60-70:\n')
           writed[0] = True
        elif i[1] > 70 and i[1] < 80 and writed[1] == False:
             fileWrite.write('\nCities that rainfall is between 70-80:\n')
             writed[1] = True
        elif i[1] > 80 and i[1] < 90 and writed[2] == False:
             fileWrite.write('\nCities that rainfall is between 80-90:\n')
             writed[2] = True
        elif i[1] > 90 and writed[3] == False:
             fileWrite.write('\nCities that rainfall is over 90:\n')
             writed[3] = True
        i[1] = str(i[1]).center(5)
        content = i[0] + i[1] + '\n'
        fileWrite.write(content)

def getkey(a):
    return a[1]

def sortList(List):
    return sorted(List, key = getkey)

def main():
    fileRead = open('rainfall.txt')
    tuple_file = readFile(fileRead)
    fileRead.close()
    sorted_file = sortList(tuple_file)
    #print(len(sorted_file))
    writeFile('rainfallfmt.txt',sorted_file)


main()