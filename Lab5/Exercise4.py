#-------------------------------------------------------------------------------
# Name:        Lab 5 Exercise4
# Purpose:
#
# Author:      Zhao
#
# Created:     06/02/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import bounded_queue
def main():
    queue = bounded_queue.BoundedQueue(3)
    request =''
    while request != 'Exit':
        request = input('Add, Serve or Exit: ').lower()
        if request not in 'addserveexit':
            print('You need to enter either Add, Serve or Exit')
            continue
        elif request == 'exit':
            print('Quitting,')
            print('Line:',queue)
            break
        elif request == 'add':
            try:
                name = input('Enter the name of the person to add: ')
                print('add ',name,' to the line.')
                queue.enqueue(name)
            except:
                print('Error: Queue is full')
                continue
            finally:
                print('people in the line:',queue)
        elif request == 'serve':
            try:
                queue.dequeue()
            except:
                print('Error: Queue is empty')
            finally:
                print('people in the line:',queue)

if __name__ == '__main__':
    main()
