#-------------------------------------------------------------------------------
# Name:        Summary Calls
# Purpose:
#
# Author:      Yizhou Zhao (Jack)
#
# Created:     11/01/2016
# Copyright:   (c) Zhao 2016
# Licence:     <yizhouZhao>
# Repository Url: https://github.com/JJack27/CMPUT175
#-------------------------------------------------------------------------------

def getInfo(file):
    return_List = []
    for i in file.readlines():
        element = []
        i = i.split(';')
        for j in i:
            if j.find('\n')>0:
               j = j[:j.find('\n')]    # Eliminating \n
            if j.find('.') != -1:   # change 'rate' from str to float
               j = float(j)
            elif len(j) <= 4:       # change 'calling_duration from str to int
                 j = int(j)
            element.append(j)
        if type(i[2]) == str:
           for x in range(3):    # add [...,number_of_calls, calling_duration,rate] to customer list
               element.append(0)
        return_List.append(element)
    return return_List

def formatPhone(phoneNumber):           # return a printable string with formated phone number
    phoneNumber = '(' + phoneNumber[:3] + ') ' + phoneNumber[3:6] + ' ' + phoneNumber[6:]
    return phoneNumber

def formatTime(time_s):                 # return a printable string with formated time
    time_h = int(time_s/3600)           # no other actions required
    time_m = int((time_s%3600)/60)
    time_s = (time_s%3600)%60
    time = [time_h, time_m, time_s]
    for i in range(3):      # add '0' if time is less than 10
        if time[i] < 10:
           time[i] = '0' + str(time[i])
        else:
             time[i] = str(time[i])
    time_print = time[0] + 'h' + time[1] + 'm' + time[2] + 's'
    return time_print

def summarizeInfo(calls, accounts):      # return a list, which each element has the following format
    for call in calls:                   # [phoneNumber, Name, callsFormed, CallingDuration, Rate]
        for account in accounts:
            if call[1] == account[0]:
               account[3] += 1
               account[4] += call[3]
               time = int(call[3]/60)
               if call[3]%60 != 0:
                   time += 1
               account[5] += time*call[4]
    for account in accounts:
        account[0] = formatPhone(account[0])
        account[1] = account[1].ljust(30)
        account[4] = formatTime(account[4])
        account[5] = str(account[5])[:str(account[5]).find('.')+3].rjust(7)
        account.remove(account[2])
    return accounts

def getkey(a):
    return a[0]

def printTableLine():
    print('+--------------+------------------------------+---+---------+--------+')

def printContentRow(content):
    if float(content[4]) > 850:
       print('|%s|%s|%s|%s|$%s|**' % (content[0],content[1],content[2],content[3],content[4]))
    elif float(content[4]) < 850 and int(content[2]) > 350:
         print('|%s|%s|%s|%s|$%s|++' % (content[0],content[1],content[2],content[3],content[4]))
    else:
         print('|%s|%s|%s|%s|$%s|' % (content[0],content[1],content[2],content[3],content[4]))

def printTable(sorted_summary):
    printTableLine()
    print('| Phone number | Name                         | # |Duration | Due    |')
    printTableLine()
    for i in sorted_summary:
        printContentRow(i)
    printTableLine()
    total = 0
    for i in sorted_summary:
        total += float(i[4])
    total = str(total)[:str(total).find('.')+3].rjust(10)
    print('| Total dues   |                                          $%s|' % (total))
    printTableLine()

def main():
    cusmoterFile = open('customers.txt')
    accounts = getInfo(cusmoterFile)
    cusmoterFile.close()

    callsFile = open('calls.txt')
    calls = getInfo(callsFile)
    callsFile.close()

    summary = summarizeInfo(calls,accounts)
    sorted_summary = sorted(summary, key = getkey)

    printTable(sorted_summary)


main()
