#-------------------------------------------------------------------------------
# Name:        Lab 8-Exercise 1
# Purpose:
#
# Author:      Zhao
#
# Created:     28/02/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def main():
    answer = random.randint(0,100)
    found = False
    for i in range(6):
        choice = input('Your Guess!')
        if choice == 'exit':
            break
        choice = int(choice)
        if choice == answer:
            print('Hooray you won!')
            found = True
            break
        elif choice > answer:
            print('Too High.')
        elif choice < answer:
            print('Too Low.')
    if not found:
        print('Ohh no you lost, the correct number is:', str(answer))


if __name__ == '__main__':
    main()
