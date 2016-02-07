#-------------------------------------------------------------------------------
# Name:        Safe Open Module
# Purpose:
#
# Author:      yizhou
#
# Created:     06/02/2016
# Copyright:   (c) yizhou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def safe_open(fileName, mode = 'both'):
    try:
        if mode == 'read':
           opened = open(fileName,'r')
        elif mode == 'write':
             opened = open(fileName,'w')
        else:
             opened = open(fileName)
    except IOError:
           print('I/O error: No such file or directory')
           return None
    else: return opened