import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        # set the value at the current node
        self.value = value
        # add ref to left child node
        self.left = None
        # add ref to the right child node
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        if self.value == target:
            return True
        else:
            if target < self.value and self.left is not None:
                return self.left.contains(target)
            elif target >= self.value and self.right is not None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        while len(children) > 0:
            for child in children:
                children.remove(child)
                if child.left is not None:
                    children.append(child.left)
                if child.right is not None:
                    children.append(child.right)
                if child.value > max_value:
                    max_value = child.value

        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        values = []
        children = []
        values.append(self.value)
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        while len(children) > 0:
            for child in children:
                children.remove(child)
                if child.left is not None:
                    children.append(child.left)
                if child.right is not None:
                    children.append(child.right)

                values.append(child.value)

        string_to_print = ""
        for index, value in enumerate(sorted(values)):
            string_to_print += str(value)
            if index != len(values) - 1:
                string_to_print += "\n"

        print(string_to_print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue data structure
        q = Queue()
        # enqueue the starting node on to the queue
        q.enqueue(node)
        # loop while the queue has data
        while q.len() > 0:
            element = q.dequeue()
            # dequeue the current it em off the queue
            # print the current value
            print(element.value)
            # if the current node has a left child
            if element.left is not None:
                # enqueue the left child on to the queue
                q.enqueue(element.left)
            # if the current node has a right child
            if element.right is not None:
                # enqueue right child on to the queue
                q.enqueue(element.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack data structure
        s = Stack()
        # push the starting node on to the stack
        s.push(node)
        # loop while the stack has data
        while s.len() > 0:
            # pop the current it em off the stack
            element = s.pop()
            # print the current value
            print(element.value)
            # if the current node has a left child
            if element.left is not None:
                # push the left child on to the stack
                s.push(element.left)
            # if the current node has a right child
            if element.right is not None:
                # push right child on to the stack
                s.push(element.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
