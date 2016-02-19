# CMPUT 175 Winter 2016 Lab 5 Exercise 3
# This file implements the Queue class and can be used to test the Queue.

class BoundedQueue:

    # Constructor, which creates a new empty queue:
    def __init__(self, capacity):
        # TODO: You must implement this constructor!
        self.__items = []
        self.__capacity = capacity
        try:
            self.__capacity = int(self.__capacity)
            if self.__capacity < 0:
                raise ValueError('the parameter capacity need to be a positive integer')
        except TypeError:
            print('Type error: capacity need to be an integer')
            raise

    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        # TODO: You must implement this method!
        if self.is_full():
            raise IndexError('The queue is full')
        self.__items.append(item)

    # Removes and returns the front-most item in the queue.
    # Returns nothing if the queue is empty.
    def dequeue(self):
        try:
            return self.__items.pop(0)
        except:
            print('The queue is empty')
            raise

    # Returns the front-most item in the queue, and DOES NOT change the queue.
    def peek(self):
        # TODO: You must implement this method!
        try:
            return self.__items[0]
        except:
            print('The queue is empty')
            raise

    # Returns True if the queue is empty, and False otherwise:
    def isEmpty(self):
        # TODO: You must implement this method!
        return self.__items == []

    def is_full(self):
        return self.size() == self.capacity()

    # Returns the number of items in the queue:
    def size(self):
        # TODO: You must implement this method!
        return len(self.__items)
    def capacity(self):
        return self.__capacity

    # Removes all items from thq queue, and sets the size to 0:
    def clear(self):
        # TODO: You must implement this method!
        self.__items = []

    # Returns a string representation of the queue:
    def __str__(self):
        # TODO: You must implement this method!
        list = self.__items
        strting = ''
        for i in list:
            strting += (i+', ')
        return strting