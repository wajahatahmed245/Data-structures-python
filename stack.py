import numpy as np


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, element_for_stack):
        self.stack_list.append(element_for_stack)

    def display_stack(self):
        stack = np.array(self.stack_list)
        print(stack)

    def pop(self):
        self.stack_list.pop()


stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.display_stack()
stack.pop()
stack.display_stack()
