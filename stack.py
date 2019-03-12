import numpy as np


class Stack:
    def __init__(self, expression_for_evaluation=" "):
        self.stack_list = []
        self.expression_for_evaluation = expression_for_evaluation

    def push(self, element_for_stack=None):
        if self.expression_for_evaluation != " ":
            for i in range(0, len(self.expression_for_evaluation)):
                self.stack_list.append(self.expression_for_evaluation[i])
        else:
            self.stack_list.append(element_for_stack)

    def display_stack(self):
        stack = np.array(self.stack_list)
        # print(stack)
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

    def priorties_operator(self, argument):
        switcher = {
            "(": 1,
            ")": 1,
            "^": 2,
            "*": 3,
            "/": 3,
            "+": 4,
            "-": 4,
        }

        return switcher.get(argument, "0")

    def infix_Postfix(self):
        Output = []
        priority = []
        stack_operator = []
        expression_array = self.display_stack()
        for i in range(0, expression_array.size):
            priority.append(self.priorties_operator(expression_array[i]))

        if priority[0] != "0":
            Output.append(" ")
            stack_operator.append(expression_array[0])
        elif priority[i] == "0":
            Output.append(expression_array[i])
            stack_operator.append(expression_array[i] - 1)

        else:
            Output.append(expression_array[i])


expression = input("write your Expression : ")
# print("lenth of string is {}".format(len(expression)))
stack = Stack(expression)

stack.push()
stack.infix_Postfix()
# for i in range(0, len(expression)):
#     stack.push(expression[i])

# stack.pop()
# stack_two = Stack()
# stack_two.push("21")
# stack_two.push("22")
# stack_two.push("31")
# stack_two.push("34")
# stack.pop()
# stack.pop()

# stack.display_stack()
# stack.reverse_stack()
