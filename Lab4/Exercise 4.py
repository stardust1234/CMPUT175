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

    c_b = True
    r_b = True
    s_b = True
    file = open(input('Enter the name of the file you want to read:'))
    str_file = readFile(file)
    for i in str_file:
        for j in range(len(i)):
            if i[j] == '(':
               i = i.replace('(', ' ', 1)
               round_bracket.push(1)
               n_rb += 1
            if i[j] == ')':
               i = i.replace(')', ' ', 1)
               if round_bracket.size() >0:
                  round_bracket.pop()
               else:
                    r_b = False
            if i[j] == '[':
               i = i.replace('[', ' ', 1)
               square_bracket.push(1)
               n_sb += 1
            if i[j] == ']':
               i = i.replace(']', ' ', 1)
               if square_bracket.size() >0:
                  square_bracket.pop()
               else:
                    s_b = False
            if i[j] == '{':
               i = i.replace('{', ' ', 1)
               curly_bracket.push(1)
               n_cb += 1
            if i[j] == '}':
               i = i = i.replace('}', ' ', 1)
               if curly_bracket.size() >0:
                  curly_bracket.pop()
               else:
                    c_b = False

    n_cb = n_cb - curly_bracket.size()
    n_sb = n_sb - square_bracket.size()
    n_rb = n_rb - round_bracket.size()

    print('() pairs: '+ str(n_rb))
    print('{} pairs: '+ str(n_cb))
    print('[] pairs: '+ str(n_sb))

    if round_bracket.size() == 0 and r_b == True:
       print('All () matched.')
    else:
         print('Not all () matched')
    if curly_bracket.size() == 0 and c_b == True:
       print('All {} matched.')
    else:
         print('Not all {} matched')
    if square_bracket.size() == 0 and s_b == True:
       print('All [] matched.')
    else:
         #print(square_bracket.size(), n_sb-int(n_sb))
         print('Not all [] matched')


main()
