#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      yizho
#
# Created:     31/01/2016
# Copyright:   (c) yizho 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import stack
def main():
    user_string = input('Enter a string to reverse:')
    string_stack = stack.Stack()
    for i in range(len(user_string)):
        string_stack.push(user_string[i])
    reversed_string = ''
    for i in range(len(user_string)):
        reversed_string += string_stack.pop()
    print(reversed_string)


if __name__ == '__main__':
    main()
