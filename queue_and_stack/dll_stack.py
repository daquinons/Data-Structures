import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(
    __file__)), '../doubly_linked_list'))
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.__len__()
