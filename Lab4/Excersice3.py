#-------------------------------------------------------------------------------
# Name:        Excercise 3
# Purpose:
#
# Author:      yizhou
#
# Created:     31/01/2016
# Copyright:   (c) yizhou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Queue:

    # Constructor, which creates a new empty queue:
    def __init__(self):
        # TODO: You must implement this constructor!
        self.__items = []

    # Adds a new item to the back of the queue, and returns nothing:
    def queue(self, item):
        # TODO: You must implement this method!
        self.__items.append(item)

    # Removes and returns the front-most item in the queue.
    # Returns nothing if the queue is empty.
    def dequeue(self):
        try:
            a = self.__items[0]
            self.__items.remove(self.__items[0])
            return a
        except: return None

    # Returns the front-most item in the queue, and DOES NOT change the queue.
    def peek(self):
        # TODO: You must implement this method!
        try:
            return self.__items[0]
        except:
               return None

    # Returns True if the queue is empty, and False otherwise:
    def is_empty(self):
        # TODO: You must implement this method!
        return self.__items == []

    # Returns the number of items in the queue:
    def size(self):
        # TODO: You must implement this method!
        return len(self.__items)

    # Removes all items from thq queue, and sets the size to 0:
    def clear(self):
        # TODO: You must implement this method!
        self.__items = []

    # Returns a string representation of the queue:
    def __str__(self):
        # TODO: You must implement this method!
        return repr(self.__items)

def main():
    lineUp = Queue()
    status = input('Add, Serve, or Exit:')
    while not (status  == 'Exit'):
          if status == 'Serve':
             if lineUp.is_empty():
                print('This lineup is already empty')
                status = input('Add Serve, or Exit:')
                continue
             print(lineUp.dequeue(), 'has been served')
             status = input('Add Serve, or Exit:')
          if status == 'Add':
             if lineUp.size() == 3:
                print("You cannot add more people, the lineup is full")
                status = input('Add Serve, or Exit:')
                continue
             lineUp.queue(input('Enter the name of the person to add:'))
             status = input('Add Serve, or Exit:')

main()
