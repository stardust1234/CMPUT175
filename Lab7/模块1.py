#-------------------------------------------------------------------------------
# Name:        妯″潡1
# Purpose:
#
# Author:      Zhao
#
# Created:     28/02/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from d_linked_list import d_linked_list
from d_linked_node import d_linked_node
def main():
    linked_list = d_linked_list()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    #linked_list.insert(0,4)
    linked_list.insert(3,5)
    print(linked_list.get_item(4))

if __name__ == '__main__':
    main()
