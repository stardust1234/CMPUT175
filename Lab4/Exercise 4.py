#-------------------------------------------------------------------------------
# Name:        Exercise 4
# Purpose:
#
# Author:      yizhou
#
# Created:     31/01/2016
# Copyright:   (c) yizhou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import stack

def readFile(file):
    str_file = []
    for i in file.readlines():
        str_file.append(i)
    return str_file

def main():
    round_bracket = stack.Stack()
    square_bracket = stack.Stack()
    curly_bracket = stack.Stack()
    n_rb = 0                     # number of round_bracket
    n_sb = 0                     # number of square_bracket
    n_cb = 0                     # number of square_bracket
    file = open(input('Enter the name of the file you want to read:'))
    str_file = readFile(file)
    for i in str_file:
        if i.find('(') >=0:
           i.replace('(', ' ', 1)
           round_bracket.push(1)
           n_rb += 1
        if i.find(')') >= 0:
           i.replace(')', ' ', 1)
           if round_bracket.size() >0:
              round_bracket.pop()
           n_rb += 1
        if i.find('[') >=0:
           i.replace('[', ' ', 1)
           square_bracket.push(1)
           n_sb += 1
        if i.find(']') >=0:
           i.replace(']', ' ', 1)
           if square_bracket.size() >0:
              square_bracket.pop()
           n_sb += 1
        if i.find('{') >=0:
           i.replace('{', ' ', 1)
           curly_bracket.push(1)
           n_cb += 1
        if i.find('}') >=0:
           i.replace('}', ' ', 1)
           if curly_bracket.size() >0:
              curly_bracket.pop()
           n_cb += 1

    n_rb = (n_rb-round_bracket.size())/2
    n_sb = (n_sb-square_bracket.size())/2
    n_cb = (n_cb-curly_bracket.size())/2
    print('() pairs: '+ str(int(n_rb)))
    print('{} pairs: '+ str(int(n_cb)))
    print('[] pairs: '+ str(int(n_sb)))

    if round_bracket.size() == 0 and n_rb-int(n_rb) ==0:
       print('All () matched.')
    else:
         print('Not all () matched')
    if curly_bracket.size() == 0 and n_cb-int(n_cb) ==0:
       print('All {} matched.')
    else:
         print('Not all {} matched')
    if square_bracket.size() == 0 and n_sb-int(n_sb) ==0:
       print('All [] matched.')
    else:
         #print(square_bracket.size(), n_sb-int(n_sb))
         print('Not all [] matched')


main()
