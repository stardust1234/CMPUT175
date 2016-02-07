# CMPUT 175 Winter 2013 Lab 4 Exercise 1
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
        except:
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
    def is_empty(self):
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
        return repr(self.__items)


# use this function to test your Bounded Queue implementation
def test():
    is_pass = True

    try:
        string_queue = BoundedQueue('wrong type')
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"

    try:
        string_queue = BoundedQueue(-1)
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"

    string_queue = BoundedQueue(3)

    is_pass = (string_queue.size() == 0)
    assert is_pass == True, "fail the test"

    is_pass = (string_queue.capacity() == 3)
    assert is_pass == True, "fail the test"

    is_pass = (string_queue.is_empty())
    assert is_pass == True, "fail the test"

    string_queue.enqueue("Hello")
    string_queue.enqueue("World")

    is_pass = (string_queue.size() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (string_queue.peek() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (string_queue.capacity() == 3)
    assert is_pass == True, "fail the test"

    is_pass = (string_queue.peek() == "Hello" and string_queue.size() == 2)
    assert is_pass == True, "fail the test"


    string_queue.enqueue("python")

    is_pass = (string_queue.is_full())
    assert is_pass == True, "fail the test"

    try:
        string_queue.enqueue("rules")
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"

    string_queue.clear()

    is_pass = (string_queue.capacity() == 3)
    assert is_pass == True, "fail the test"

    try:
        string_queue.dequeue()
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"

    try:
        string_queue.peek()
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"

    int_queue = BoundedQueue(2000)
    for i in range(0, 1000):
        int_queue.enqueue(i)
    correctOrder = True
    for i in range(0, 200):
        if int_queue.dequeue() != i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_queue.size() == 800)
    assert is_pass == True, "fail the test"

    is_pass = (int_queue.capacity() == 2000)
    assert is_pass == True, "fail the test"

    is_pass = (int_queue.peek() == 200)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print ("=========== cong, your implementation passes the test ============")


#let's test it
if __name__ == '__main__':
    test()