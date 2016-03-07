#-------------------------------------------------------------------------------
# Name:        Lab 8-Exercise 2
# Purpose:
#
# Author:      Zhao
#
# Created:     07/03/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def main():
    answer = random.randint(0,100)
    #print(answer)
    mode = input('User or Computer:')
    found = False
    high = 100
    low = 0
    while not found and mode == 'Computer':
        guess = (high+low)//2
        print('Computer Guess:',str(guess))
        if guess == answer:
            print('Hooray you won!')
            found = True
        elif guess > answer:
            print('-')
            high = guess
        elif guess < answer:
            print('+')
            low = guess


    if mode == 'User':
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
