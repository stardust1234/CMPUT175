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
        date = []
        date.append(int(i[1].split('/')[0]))
        date.append(int(i[1].split('/')[1]))
        date.append(int(i[1].split('/')[2]))
        dates.append(date)
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
        for month in range(1,13):
            for year in range(1900,2100):
                dailyEarthquake = []
                for i in sortedFile:
                    if date == i[2][2] and month == i[2][1] and year == i[2][0]:
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
    #print(sortedFile)
    formatedFile = formatFile(sortedFile)
    print(formatedFile)

main()