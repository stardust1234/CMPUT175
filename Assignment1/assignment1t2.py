#-------------------------------------------------------------------------------
# Name:        Task 2
# Purpose:
#
# Author:      Zhao
#
# Created:     11/01/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def getInfo(file):
    return_List = []
    index = 1
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
        element.insert(str(index))
        index += 1
        return_List.append(element)
    return return_List

def main():
    customerFile = open('customer.txt')
    nodes = getInfo(customerFile)
    print(nodes)

if __name__ == '__main__':
    main()
