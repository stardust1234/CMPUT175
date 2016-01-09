#-------------------------------------------------------------------------------
# Name:        Earthquake
# Purpose:
#
# Author:      Zhao
#
# Created:     08/01/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def readFile(fileName):
    file = []
    for i in fileName.readlines():
        file.append(i.split(' ', 3)[:2])
    return file

def getDates(dateList):
    dates = []
    for i in dateList:
        dates.append(int(i[1].split('/')[2]))
    return dates

def getKey(a):
    return a[2]

def sortByDate(readFile):
    dates = getDates(readFile)
    for i in range(len(dates)):
        readFile[i].append(dates[i])
    return sorted(readFile, key = getKey)

def formatFile(sortedFile):
    summary = []
    for date in range(1,32):
        dailyEarthquake = []
        for i in sortedFile:
            if date == i[2]:
               if dailyEarthquake == []:
                  dailyEarthquake.append(i[1])
               dailyEarthquake.append(i[0])
        if not dailyEarthquake==[]:
           summary.append(dailyEarthquake)
    return summary

def main():
    fileRead = open('earthquake.txt')
    read = readFile(fileRead)
    sortedFile = sortByDate(read)
    formatedFile = formatFile(sortedFile)
    print(formatedFile)

main()