from d_linked_list import d_linked_list
from d_linked_node import d_linked_node

class m_sorted_list:

    def __init__(self, m_sorted):
        self.__items = d_linked_list()
        self.__head = None
        self.__tail = None
        self.__m_sorted = m_sorted
        self.__size = 0

    def add(self, item):
        temp = d_linked_node(item, None, None)
        if self.__m_sorted:
            if self.__size == 0:
                self.__items.add(item)
            else:
                pos = self.__items.search_larger(item)
                #print(item, pos)
                if pos == -1:
                    self.__items.append(item)
                elif pos == 0:
                    self.__items.add(item)
                else:
                    self.__items.insert(pos, item)
            self.__size += 1
        else:
            self.__items.append(item)
            self.__size += 1


    def pop(self):
        if self.__m_sorted:
            self.__size -= 1
            return self.__items.pop1()
        else:
            self.__size -= 1
            return self.__items.pop(0)


    def search(self, item):
        # TODO:
        found = self.__items.search(item)
        index = 0
        if found:
            #print(self.__size)
            for i in range(self.__size-1):
                if self.__items.get_item(i) == item:
                    index = i
        else:
            if self.__m_sorted:
                index = self.__items.search_larger(item)
            else:
                index = -1
        return (found, index)

    def change_sorted(self):
        '''
        self.__m_sorted = True
        a = self.__items
        for i in range(self.__size):
            temp = self.pop()
            self.add(temp)
            '''
        if self.__m_sorted == True:
            self.__m_sorted = False
        else:
            raise Exception('I do not know how to sort a doubly linked yet.')


    def get_size(self):
        return self.__size

    def get_item(self, pos):
        return self.__items.get_item(pos)

    def __str__(self):
        return str(self.__items)

def test():

    sor_list = m_sorted_list(True)

    is_pass = (sor_list.get_size() == 0)
    assert is_pass == True, "fail the test"

    sor_list.add(4)
    sor_list.add(3)
    sor_list.add(8)
    sor_list.add(7)
    sor_list.add(1)

    is_pass = (str(sor_list) == "1 3 4 7 8")
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_size() == 5)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.pop() == 8)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.pop() == 7)
    assert is_pass == True, "fail the test"

    is_pass = (str(sor_list) == "1 3 4")
    assert is_pass == True, "fail the test"

    a = sor_list.search(2)
    is_pass = (a[0] == False and a[1] == 1)
    assert is_pass == True, "fail the test"

    a = sor_list.search(3)
    is_pass = (a[0] == True and a[1] == 1)
    assert is_pass == True, "fail the test"

    a = sor_list.search(7)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_size() == 3)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_item(2) == 4)
    assert is_pass == True, "fail the test"

    sor_list.change_sorted()
    sor_list.add(1)

    is_pass = (str(sor_list) == "1 3 4 1")
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_size() == 4)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.pop() == 1)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.pop() == 3)
    assert is_pass == True, "fail the test"

    sor_list.add(7)
    sor_list.add(6)

    is_pass = (str(sor_list) == "4 1 7 6")
    assert is_pass == True, "fail the test"

    a = sor_list.search(2)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"

    a = sor_list.search(7)
    is_pass = (a[0] == True and a[1] == 2)
    assert is_pass == True, "fail the test"

    a = sor_list.search(8)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_size() == 4)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list.get_item(2) == 7)
    assert is_pass == True, "fail the test"


    sor_list2 = m_sorted_list(False)

    is_pass = (sor_list2.get_size() == 0)
    assert is_pass == True, "fail the test"

    sor_list2.add(4)
    sor_list2.add(3)
    sor_list2.add(8)
    sor_list2.add(7)
    sor_list2.add(1)

    is_pass = (str(sor_list2) == "4 3 8 7 1")
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.get_size() == 5)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.pop() == 4)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.pop() == 3)
    assert is_pass == True, "fail the test"

    is_pass = (str(sor_list2) == "8 7 1")
    assert is_pass == True, "fail the test"

    a = sor_list2.search(2)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"

    a = sor_list2.search(7)
    is_pass = (a[0] == True and a[1] == 1)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.get_size() == 3)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.get_item(2) == 1)
    assert is_pass == True, "fail the test"

    try:
        sor_list2.change_sorted()
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"


    sor_list2.add(3)
    sor_list2.add(2)

    is_pass = (str(sor_list2) == "8 7 1 3 2")
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.get_size() == 5)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.pop() == 8)
    assert is_pass == True, "fail the test"

    is_pass = (sor_list2.pop() == 7)
    assert is_pass == True, "fail the test"


    is_pass = (str(sor_list2) == "1 3 2")
    assert is_pass == True, "fail the test"


    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

if __name__ == '__main__':
    test()
