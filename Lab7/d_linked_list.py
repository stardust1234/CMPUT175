from d_linked_node import d_linked_node

class d_linked_list:

    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0


    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index

    def add(self, item):
        temp = d_linked_node(item,self.__head,None)
        temp.setNext(self.__head)
        if self.__head != None:
            self.__head.setPrevious(temp)
        else:
            self.__tail = temp
        self.__head = temp
        self.__size += 1

    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if current.getData() == None:
                return 0
        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if current.getNext() != None:
            current.getNext().setPrevious(previous)
        else:
            self.__tail = previous
        self.__size -= 1

    def append(self, item):
        temp = d_linked_node(item, None, None)
        if self.__size == 0:
            self.__head = temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail = temp
        self.__size += 1

    def insert(self, pos, item):
        if pos > self.__size:
            raise Exception('Index out of range!')
        temp = d_linked_node(item, None, None)
        current = self.__head
        previous = None
        for i in range(pos):
            previous = current
            current = current.getNext()
        if previous == None:
            self.__head = temp
            temp.setPrevious(None)
            temp.setNext(current)
            current.setPrevious(temp)
        elif current == None:
            temp.setPrevious(previous)
            previous.setNext(temp)
            self.__tail = temp
        else:
            temp.setNext(current)
            temp.setPrevious(previous)
            previous.setNext(temp)
            current.setPrevious(temp)
        self.__size += 1

    def pop1(self):
        temp = self.__tail
        previous = self.__tail.getPrevious()
        # temp.setPrevious(None)
        if self.__size > 1:
            previous.setNext(None)
        self.__tail = previous
        self.__size -= 1
        return temp.getData()


    def pop(self, pos):
        if pos >= self.__size:
            raise Exception('Index out of range!')
        current = self.__head
        previous = None
        for i in range(pos):
            previous = current
            current = current.getNext()
        if previous == None:
            self.__head = current.getNext()
            self.__head.setPrevious(None)
        elif current.getNext() == None:
            previous.setNext(None)
            self.__tail = previous
        else:
            previous.setNext(current.getNext())
            current.getNext().setPrevious(previous)
        self.__size -= 1
        return current.getData()


    def search_larger(self, item):
        current = self.__head
        for i in range(self.__size):
            if current.getData() > item:
                return i
            current = current.getNext()
        return -1

    def get_size(self):
        return self.__size

    def get_item(self, pos):
        if pos < 0:
            pos = self.__size + pos
        if pos == self.__size:
            return None
        elif pos > self.__size:
            raise Exception('Index out of range!')
        current = self.__head
        item = None
        for i in range(pos+1):
            item = current.getData()
            current = current.getNext()
        return item

    def __str__(self):
        str_express = ''
        current = self.__head
        for i in range(self.__size):
            if i < self.__size -1:
                str_express += str(current.getData()) + ' '
            else:
                str_express += str(current.getData())
            current = current.getNext()
        return str_express



def test():

    linked_list = d_linked_list()

    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add("World")
    linked_list.add("Hello")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"


    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop1() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = d_linked_list()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"

    int_list = d_linked_list()

    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"



    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"


    for i in range(0, 200):
        if int_list.pop1() != 999 - i:
            print(int_list.pop1(), str(999-i))
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test"

    int_list.insert(7,801)

    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"


    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 1! ============")

if __name__ == '__main__':
    test()