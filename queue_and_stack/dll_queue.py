import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(
    __file__)), '../doubly_linked_list'))
from doubly_linked_list import DoublyLinkedList



class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.__len__()
