#-------------------------------------------------------------------------------
# Name:        Exercise 2: Grocery Lineup
# Purpose:
#
# Author:      Zhao
#
# Created:     19/02/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import circular_queue
def main():
    normal_queue = circular_queue.CircularQueue(3)
    vip_queue = circular_queue.CircularQueue(3)
    request = ''
    while request != 'exit':
        request = input('Add, Serve or Exit: ').lower()
        if request not in 'addserveexit':
            print('You need to enter either Add, Serve or Exit')
            continue
        elif request == 'exit':
            print('Quitting')
            break
        elif request == 'add':
            try:
                name = input('Enter the name of the person to add: ')
                is_vip = input('Is the customer VIP?(True/False)').lower()
                if is_vip not in 'truefalse':
                    raise Exception('You need to enter True or False')
                if is_vip == 'true':
                    vip_queue.enqueue(name)
                    print('Add ',name,' to the VIP line.')
                elif is_vip == 'false':
                    normal_queue.enqueue(name)
                    print('Add ',name,' to the normal line.')
            except:
                if vip_queue.isFull():
                    print('Error: The VIP queue is full')
                if normal_queue.isFull():
                    print('Error: The normal queue is full')
                continue
            finally:
                print('People in normal line:',normal_queue)
                print('People in VIP line:',vip_queue)
        elif request == 'serve':
            try:
                if vip_queue.isEmpty():
                    print(normal_queue.dequeue(),'has been served.')
                else:
                    print(vip_queue.dequeue(),'has been served.')
            except:
                print('Error: Queues are empty')
            finally:
                print('People in normal line:',normal_queue)
                print('People in VIP line:',vip_queue)



if __name__ == '__main__':
    main()
