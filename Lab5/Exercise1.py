#-------------------------------------------------------------------------------
# Name:        Exercise 1: Safe Open
# Purpose:
#
# Author:      yizhou
#
# Created:     06/02/2016
# Copyright:   (c) yizhou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def safe_open(fileName, mode):
    try:
        if mode == 'read':
           open(fileName,'r')
        elif mode == 'write':
             open(fileName,'w')
        elif mode == 'both':
             open(fileName)
    except IOError:
           print('I/O error: No such file or directory')
           return None
    else: return True

def main():
    fileName =input('Enter the file name to read:')
    mode = input('For reading or writing or both?\nEnter \'read\',\'write\', or \'both\'')
    while mode not in 'readwriteboth':
          print('Invalid input, please check your spell.')
          mode = input('For reading or writing or both?\nEnter \'read\',\'write\', or \'both\'')
    f = safe_open(fileName, mode)
    print('f == None:', f==None)

if __name__ == '__main__':
    main()
