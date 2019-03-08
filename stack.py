import numpy as np


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, element_for_stack):
        self.stack_list.append(element_for_stack)

    def display_stack(self):
        stack = np.array(self.stack_list)
        print(stack)
        return stack

    def pop(self):
        if not self.stack_list:
            print("stack underflow")
        else:
            top = len(self.stack_list) - 1
            removed_elements = self.stack_list[top]
            print("The element {} is removed".format(removed_elements))
            self.stack_list.pop()

    def reverse_stack(self):
        reversed_arr = self.display_stack()[::-1]
        print("The reverse of stack is {}".format(reversed_arr))


stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.display_stack()
stack.pop()
stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
stack.push(7)
stack.push(10)
stack.display_stack()
stack.reverse_stack()