#-------------------------------------------------------------------------------
# Name:        Circular Queue
# Purpose:
#
# Author:      Zhao
#
# Created:     19/02/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class CircularQueue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception('Capacity Error!')
        self.__item = []
        self.__capacity = capacity
        self.__head = 0
        self.__tail = 0
        self.__count = 0

    def enqueue(self,item):
        if self.__count == self.__capacity:
            raise Exception('Error: Queue is full!')
        if len(self.__item) < self.__capacity:
            self.__item.append(item)
        else:
            self.__item[self.__tail] = item
        self.__count += 1
        self.__tail = (self.__tail+1)%self.__capacity

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Error: Queue is empty!')
        item = self.__item[self.__head]
        self.__item[self.__head] = None
        self.__count -= 1
        self.__head =(self.__head+1)%self.__capacity
        return item

    def peek(self):
        if self.isEmpty():
            raise Exception('Error: Queue is empty!')
        return self.__item[self.__head]

    def isEmpty(self):
        return self.__count == 0

    def isFull(self):
        return self.__count == self.__capacity

    def capacity(self):
        return self.__capacity

    def clear(self):
        self.__item = []

    def __str__(self):
        string = ''
        for i in self.__item:
            if i == None:
                i = ''
            string += (str(i)+' ')
        return string