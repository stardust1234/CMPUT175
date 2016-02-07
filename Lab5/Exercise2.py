#-------------------------------------------------------------------------------
# Name:        Exercise 2
# Purpose:
#
# Author:      yizho
#
# Created:     06/02/2016
# Copyright:   (c) yizho 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import safeOpen

def putInList(listToSplit, seperator):
    listToPut = []
    for i in listToSplit:
        i = i.split(seperator)
        for j in i:
            listToPut.append(j)
    return listToPut

# This method would turn all the character to lower cases, and split the file by space, comma and quote
def cleanFile(file):
    fileToReturn = []
    woutSpace = putInList(file.readlines(),' ')
    woutColon = putInList(woutSpace, ':')
    woutComma = putInList(woutColon, ',')
    woutPeriod = putInList(woutComma, '.')
    woutQoute = putInList(woutPeriod, '\'')
    woutDoubleQoute = putInList(woutQoute,'\"')
    for i in range(len(woutDoubleQoute)):
        woutDoubleQoute[i] = woutDoubleQoute[i].lower()
        woutDoubleQoute[i] = woutDoubleQoute[i].rstrip()
    for i in woutDoubleQoute:
        if i != '':
           fileToReturn.append(i)
    return fileToReturn

def summarizeFile(fileInLine):
    dic = {}
    for i in fileInLine:
        try:
            dic[i]+=1
        except:
               dic[i] = 1
    return dic

def main():
    fileName = input('Enter the to-be opened file name:')
    file = safeOpen.safe_open(fileName)
    fileInLine = cleanFile(file)
    summary = summarizeFile(fileInLine)
    for i in summary.keys():
        print(i,str(summary[i]), sep = ':')


if __name__ == '__main__':
    main()
