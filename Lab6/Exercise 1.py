#-------------------------------------------------------------------------------
# Name:        Exercise 1: Test Queues
# Purpose:
#
# Author:      Zhao
#
# Created:     19/02/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import circular_queue, bounded_queue, time

def dqRuntime(queue):
    start = time.time()
    while not queue.isEmpty():
        queue.dequeue()
    end = time.time()
    return end-start

def addItemsToQueue(queue, items):
    if queue.capacity() != len(items):
        raise Exception('Error: Length of items is not equal to the capacity of queue')
    for i in items:
        queue.enqueue(i)
    return queue

def main():
    items = []
    for i in range(10000):
        items.append(i)

    b_queue = bounded_queue.BoundedQueue(len(items))
    c_queue = circular_queue.CircularQueue(len(items))
    b_queue = addItemsToQueue(b_queue, items)
    c_queue = addItemsToQueue(c_queue, items)
    runtimeForBq = dqRuntime(b_queue)
    runtimeForCq = dqRuntime(c_queue)
    print('Bounded Queue:    ',runtimeForBq)
    print('Circular Queue:   ',runtimeForCq)
    print('It is',str(runtimeForBq>runtimeForCq),'that dequeue in circular queue is much faster than that in bounded queue.')
if __name__ == '__main__':
    main()
